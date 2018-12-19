# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'C:\Users\Python\Desktop\asd\.eric6project\login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import os

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QIcon, QFont
from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QWidget, QGridLayout, QLineEdit

VIEWS = '/home'


class BaseLoginWindow(QWidget):
    # 登录失败信号
    login_f = pyqtSignal(str)

    def setup_ui(self):
        self.setObjectName("Form")
        self.resize(300, 200)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(110, 30, 161, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 60, 161, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.checkBox = QtWidgets.QCheckBox(self)
        self.checkBox.setGeometry(QtCore.QRect(110, 80, 71, 31))
        self.checkBox.setObjectName("checkBox")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(20, 120, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 120, 111, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(200, 80, 54, 31))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 20, 81, 81))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/user/10.jpg"))
        self.label.setObjectName("label")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/logo/chatting1.ico"))
        self.setWindowIcon(icon)
        QtCore.QMetaObject.connectSlotsByName(self)

        # copy
        self.lineEdit.setPlaceholderText('账号')
        self.lineEdit_2.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit_2.setPlaceholderText("密码6~15位，由字母、数字组成")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        grid = QGridLayout()
        # 第x行，第x列开始，占x行、x列
        grid.addWidget(self.label, 0, 0, 4, 1)
        grid.addWidget(self.lineEdit, 1, 1, 1, 2)
        grid.addWidget(self.lineEdit_2, 2, 1, 1, 2)
        grid.addWidget(self.pushButton, 4, 1, 1, 1)
        grid.addWidget(self.pushButton_2, 4, 2, 1, 1)
        grid.addWidget(self.checkBox, 3, 1, 1, 2)
        # grid.addWidget(self.label_3, 2,2,1,1)
        grid.setHorizontalSpacing(10)
        grid.setVerticalSpacing(10)
        grid.setContentsMargins(10, 10, 10, 10)
        self.setLayout(grid)

        font = QFont()
        font.setPointSize(9)
        self.checkBox.setFont(font)
        self.lineEdit_2.setFont(font)

        # 让窗口固定
        self.setFixedSize(275, 179)

        self.retranslate_ui()

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "登录"))
        self.checkBox.setText(_translate("self", "记住密码"))
        self.pushButton.setText(_translate("self", "登录"))
        self.pushButton_2.setText(_translate("self", "注册"))
        # self.label_3.setText(_translate("self", "忘记密码？"))


