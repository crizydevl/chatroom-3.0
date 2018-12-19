import json
import socket
import sys
import copy
from chat_window import *
from PyQt5.QtCore import QThread, Qt
from select import select


class MyThread(QThread):

    def __init__(self, client, parent=None):
        super().__init__(parent)
        self.client = client

    def run(self):
        print('threading')
        try:
            self.client.get_msg()
        except:
            sys.exit()


class Client(object):

    def __init__(self):
        self.create_tcp_socket()
        self.create_udp_socket()
        self.create_login_window()
        self.main_window = MainWindow(self.tcp_sock, self.udp_sock)

    def create_tcp_socket(self):
        '''创建tcp套接字'''
        self.tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_sock.connect(('176.221.12.35', 9999))

    def create_udp_socket(self):
        '''创建udp套接字'''
        # 获取tcp的地址
        self.addr, self.tcp_port = self.tcp_sock.getsockname()
        self.udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_port = self.tcp_port + 1
        while True:
            try:
                self.udp_sock.bind((self.addr, self.udp_port))
                break
            except OSError:
                self.udp_port += 1
        print(self.addr, self.udp_port)

    def create_login_window(self):
        '''显示登录窗口'''
        self.login_window = LoginWindow(self.tcp_sock, self.udp_sock)
        self.login_window.show()

    def get_msg(self):
        '''io多路复用对tcp和udp套接字信息进行监控'''
        while True:
            read_list, _, __ = select([self.tcp_sock, self.udp_sock], [], [])
            for i in read_list:
                if i == self.tcp_sock:
                    data = i.recv(2048).decode('utf-8')
                    # 收到tcp信息交给tcp_hander的方法处理
                    self.tcp_hander(data)
                elif i == self.udp_sock:
                    data, addr = i.recvfrom(2048)
                    # 收到udp信息交给udp_hander的方法处理
                    self.udp_hander(data)

    def tcp_hander(self, recv_data):
        '''处理tcp请求的方法'''
        data = json.loads(recv_data)
        if data.get('T') == 'login':
            if data['state'] == '1':
                # 登录成功后logib_window的close_code改为1
                self.login_window.close_code = 1
                if self.login_window.checkBox.checkState() == Qt.Checked:
                    self.login_window.remeber_pwd(data['head'])
                else:
                    f = open('users.txt', 'w')
                    f.close()
                # 关闭登录框
                self.login_window.close()
                data.pop('T')
                data.pop('state')
                # 显示主界面, 发送信号,并未主窗口创建myinfo属性
                self.main_window.myinfo = data
                self.main_window.show_window_singal.emit(data['userid'], data['name'], data['head'], data['email'])
                self.tcp_sock.send(json.dumps({'T': 'ADDR', 'addr': (self.addr, self.udp_port)}).encode('utf-8'))
            elif data['state'] == '0':
                # 登录失败发送登录失败信号
                self.login_window.login_f[str].emit(data['msg'])

        elif data.get('T') == 'regist':
            if data['state'] == '1':
                self.login_window.register_window.regist_s.emit(data['userid'])

        elif data.get('T') == 'email':
            code = data['code']
            # 注册框的email_code重新赋值
            self.login_window.register_window.email_code = code

        elif data.get('T') == 'FL':
            self.friend_list = data.get('content')
            # 给主窗口的好友列表重新赋值
            self.main_window.create_group_singal.emit(self.friend_list, '1')
            self.tell_friend_online()
        elif data.get('T') == 'UR':
            self.main_window.get_unread_msg_singal.emit(data['content'])

        elif data.get('T') == 'AF':
            if data['state'] == '1':
                # self.friend_list.append(data['content'][0])
                print(data['content'])
                self.friend_list += data['content']
                self.main_window.create_group_singal.emit(data['content'], '0')
                if data['content'][0]['state'] == '1':

                    myinfo = copy.deepcopy(self.main_window.myinfo)
                    myinfo['friendid'] = self.main_window.myinfo['userid']
                    myinfo.pop('userid')
                    myinfo.update({'addr': (self.addr, self.udp_port), 'state': '1'})
                    msg = {'T': 'AF', 'state': '1', 'content': [myinfo]}
                    self.udp_sock.sendto(json.dumps(msg).encode('utf-8'), tuple(data['content'][0]['addr']))
                    del myinfo
            elif data['state'] == '0':
                self.main_window.add_friend_fail_singal.emit(data['msg'])

    def udp_hander(self, recv_data):
        '''处理udp请求的方法'''
        data = json.loads(recv_data.decode('utf-8'))
        if data['T'] == 'online':
            self.main_window.change_friend_state_singal.emit('1', data['friendid'], data['addr'])

            for i in self.friend_list:
                if i['friendid'] == data['friendid']:
                    i['state'] = '1'
                    i['addr'] = data['addr']
                    break

        elif data['T'] == 'SC':
            self.main_window.chat_window_dict[data['friendid']].get_new_msg(data['content'], data['time'])

        elif data['T'] == 'offline':
            self.main_window.change_friend_state_singal.emit('0', data['friendid'], [])
            for i in self.friend_list:
                if i.get('friendid') == data['friendid']:
                    i['state'] = '0'
                    break

        elif data['T'] == 'AF':
            print('44444', data)
            self.friend_list += data['content']
            self.main_window.create_group_singal.emit(data['content'], '0')

    def tell_friend_online(self):
        msg = json.dumps({'T': 'online', 'friendid': self.main_window.myinfo['userid'], 'addr': (self.addr, self.udp_port)}).encode('utf-8')

        for i in self.friend_list:
            if i['state'] == '1':
                addr = tuple(i['addr'])
                self.udp_sock.sendto(msg, addr)

    def tell_friend_offline(self):
        msg = {'T': 'offline', 'friendid': self.main_window.myinfo['userid']}
        for i in self.friend_list:
            print(i['addr'], i['state'])
            if i['state'] == '1':
                print(i['addr'])
                addr = tuple(i['addr'])
                self.udp_sock.sendto(json.dumps(msg).encode('utf-8'), addr)