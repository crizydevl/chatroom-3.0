import json
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox

from .base_window.login_view import BaseLoginWindow
from .register_window import RegisterDialog


class LoginWindow(BaseLoginWindow):

    def __init__(self, tcp_socket, udp_socket):
        super().__init__()
        self.tcp_sock = tcp_socket
        self.udp_sock = udp_socket
        # 默认close_code为0,当登录成功的时候，close_code改为1，由此判断关闭本窗口还是退出整个程序
        self.close_code = 0
        self.setup_ui()
        self.connect_func()
        self.isremeber_pwd()

    def connect_func(self):
        '''初始化注册信号与相关槽函数'''
        # 注册按钮
        self.pushButton_2.clicked.connect(self.create_register_window)
        # 登录按钮
        self.pushButton.clicked.connect(self.login)
        # 注册登录失败信号注册槽函数
        self.login_f.connect(self.login_failed)
        # 登录时判断是否记住密码

    @staticmethod
    def json_encode_msg(msg):
        '''序列化并解码信息字典'''
        return json.dumps(msg).encode('utf-8')

    def create_register_window(self):
        '''创建登录窗口'''
        self.register_window = RegisterDialog(self.tcp_sock)
        self.register_window.connect_func()
        print('dasdsgdsgdsfgdsf')
        self.register_window.show()

    def login(self):
        '''发送账号密码等登录信息'''
        try:
            userid = int(self.lineEdit.text())
            passwd = self.lineEdit_2.text()
        except ValueError:

            QMessageBox.critical(self, '账号错误', '请输入纯数字组成的账号')
            return
        send_msg = {'T': 'login', 'userid': userid, 'passwd': passwd}
        msg = self.json_encode_msg(send_msg)
        self.tcp_sock.send(msg)

    def login_failed(self, data):
        '''登录失败的弹出框提示'''
        QMessageBox.critical(self, '登录失败', data)

    def closeEvent(self, event):
        '''重写close事件函数'''
        print('退出')
        if self.close_code == 0:
            # 关闭udp和tcp套接字并退出程序
            self.tcp_sock.close()
            self.udp_sock.close()
            sys.exit(0)
        elif self.close_code == 1:
            event.accept()

    def remeber_pwd(self, head):
        # 设置记住密码
        userid = self.lineEdit.text()
        passwd = self.lineEdit_2.text()
        if self.checkBox.checkState() == Qt.Checked:
            data = '#'.join(['1', userid, passwd, head])
            with open('users.txt', 'w') as f:
                f.write(data)

    def isremeber_pwd(self):
        # 启动时判断是否记住密码
        with open('users.txt', 'r') as f:
            data = f.read()
            if data:
                data = data.split('#')
                if data[0] == '1':
                    self.checkBox.setChecked(True)
                    self.lineEdit.setText(data[1])
                    self.lineEdit_2.setText(data[2])
                    self.label.setPixmap(QPixmap("images/user/%s" % data[3]))

                else:
                    self.checkBox.setChecked(False)
