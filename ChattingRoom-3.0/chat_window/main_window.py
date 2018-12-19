import json

from PyQt5.QtWidgets import QApplication, QMessageBox
from qtpy import QtGui

from .base_window.main_window_view import BaseMainWindow
from .chat_window import ChatWindow


class MainWindow(BaseMainWindow):

    def __init__(self, tcp, udp):
        super().__init__()
        # 初始化小部件
        self.tcp = tcp
        self.udp = udp
        self.setup_ui()
        # 初始化信号与槽的注册
        self.connect_func()
        # 默认好友列表的信息存储容器为一个空列表
        self.friend_list = []
        self.chat_window_dict = {}

    def connect_func(self):
        '''初始化信号与槽的注册'''
        # show_window信号与show函数注册
        self.show_window_singal.connect(self.show_window)
        self.create_group_singal.connect(self.create_group)
        self.change_friend_state_singal.connect(self.change_friend_state)
        self.get_unread_msg_singal.connect(self.handle_unread_msg)
        self.tb_add.clicked.connect(self.add_friend)
        self.add_friend_singal.connect(self.add_new_friend)
        self.add_friend_fail_singal.connect(self.add_friend_fail)

    def show_window(self, userid, name, head, email):
        self.lb_name.setText(name)
        self.lb_id.setText(str(userid))
        self.lb_head.setPixmap(QtGui.QPixmap("images/user/%s" % head))
        self.lb_email.setText(email)
        self.show()

    def create_group(self, friend_list, num):
        '''创建"我的好友"分组及其列表的好友图标'''
        if num == "1":
            self.friend_list = friend_list
            self.group.set_child(self.friend_list, '1')
        elif num == '0':
            self.friend_list += friend_list
            self.group.set_child(friend_list, '0')

        for i in self.friend_list:
            # 为每个好友创建聊天窗口
            chat = ChatWindow(self, self.tcp, self.udp, i['name'], i['addr'], i['friendid'], self.myinfo['userid'], i['state'])
            self.chat_window_dict[i['friendid']] = chat

    def change_friend_state(self, statecode, friendid, addr):
        '''改变好友状态'''
        self.group.frienddic[friendid].set_state(statecode)
        # 修改窗口的addr属性
        if addr:
            self.chat_window_dict[friendid].addr = tuple(addr)
            self.chat_window_dict[friendid].state = '1'

        if statecode == '1':
            self.group.change_online_num('1')
        elif statecode == '0':
            self.group.change_online_num('0')

    def show_chat_window(self):
        # 双击弹出聊天框图标
        print(self.chat_window_dict)
        hititem = self.treeWidget.currentItem()
        self.treeWidget.clearSelection()
        '''显示相应聊天对象的聊天窗口'''
        self.chat_window_dict[hititem.userid].show()

    def handle_unread_msg(self, unread_list):
        '''处理未读消息'''
        for i in unread_list:
            QApplication.processEvents()
            self.chat_window_dict[i['friendid']].get_new_msg(i['content'], i['time'])
        self.treeWidget.doubleClicked.connect(self.show_chat_window)

    def add_friend(self):
        '''添加好友'''
        friend_num = int(self.lineEdit.text())
        msg = json.dumps({'T': 'AF', 'friendid': friend_num}).encode('utf-8')
        self.tcp.send(msg)

    def add_new_friend(self, info):
        print(info)
        for i in self.friend_list:
            # 为每个好友创建聊天窗口
            chat = ChatWindow(self, self.tcp, self.udp, i['name'], i['addr'], i['friendid'], self.myinfo['userid'], i['state'])
            self.chat_window_dict[i['friendid']] = chat
            self.group.add_friend(i['state'])
        self.friend_list += info

    def add_friend_fail(self, msg):
        QMessageBox.warning(self, '提示', msg)