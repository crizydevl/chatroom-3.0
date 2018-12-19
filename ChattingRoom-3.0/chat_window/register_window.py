import json
import random
import re

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMessageBox

from .base_window.register_view import BaseRegisterDialog


class RegisterDialog(BaseRegisterDialog):

    def __init__(self, tcp_sock):
        super().__init__()
        self.tcp_sock = tcp_sock
        self.setupUi()
        # 初始化默认邮箱的验证码为0
        self.email_code = 0

    def connect_func(self):
        '''信号与槽函数注册'''
        # 注册成功信号
        print('注册前')
        self.regist_s.connect(self.regist_success)
        # 注册验证密码的槽信号
        self.lineEdit_7.editingFinished.connect(self.verfiry_password)
        # 获取验证码按钮
        self.pushButton_2.clicked.connect(self.send_mail)
        self.pushButton.clicked.connect(self.register)

    @staticmethod
    def content_json_encode(content):
        '''序列化＋转码方法'''
        return json.dumps(content).encode('utf-8')

    def send_mail(self):
        # 获取邮箱输入框中的邮箱地址
        email = self.lineEdit_4.text()
        # 验证邮箱是否输入符合格式
        res = re.match(r'.*@.*?\..*', email)
        if not res:
            QMessageBox.critical(self, '错误', '邮箱格式错误')
            return
        content = {'T': 'EMAIL', 'email': email}
        content = self.content_json_encode(content)
        # 发送消息
        self.tcp_sock.send(content)
        self.pushButton_2.setText('已发送')

    def email_code_verfiry(self):
        '''邮箱验证码验证'''
        print(self.email_code, 'email_code')
        if self.email_code != 0:
            input_code = self.lineEdit_5.text()
            if input_code != str(self.email_code):
                QMessageBox.critical(self, '错误', '您输入的验证码错误')
            else:
                return True

    def register(self):
        # 注册方法
        print('注册中')
        if not self.email_code_verfiry():
            return
        if self.verfiry_password() == 0:
            QMessageBox.critical(self, '注册失败', '两次密码不一致')
            return
        name = self.lineEdit_6.text()
        age = self.lineEdit.text()
        sex = self.radioButton.text() if self.radioButton.isChecked() else self.radioButton_2.text()
        passwd = self.lineEdit_3.text()
        email = self.lineEdit_4.text()
        head = str(random.randint(0,25)) + '.jpg'
        # data['passwd'], data['name'], data['age'], data['sex'], data['email']
        content = dict(T='regist', passwd=passwd, name=name, sex=sex, email=email, age=age, head=head)
        print(content, '1111111111111111register')
        content = self.content_json_encode(content)
        # 发送消息
        self.tcp_sock.send(content)

    def regist_success(self, num):
        QMessageBox.information(self, '注册成功', '您的账号是：%d' % num, QMessageBox.Yes)

    def verfiry_password(self):
        '''验证两次密码是否匹配'''

        if not self.lineEdit_3.text() and not self.lineEdit_7.text():
            QMessageBox.critical(self, '密码错误', '密码不能为空')
            return
        else:
            if self.lineEdit_3.text() == self.lineEdit_7.text():
                self.label_6.setPixmap(QPixmap('images/tubiao/yes1.jpg'))
                return True
            else:
                self.label_6.setPixmap(QPixmap('images/tubiao/no1.jpg'))
                return 0
