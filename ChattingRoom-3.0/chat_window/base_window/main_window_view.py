# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'F:\PyQt5\PyQt540\ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow


class BaseMainWindow(QMainWindow):
    # 创建一个显示窗口的信号
    show_window_singal = pyqtSignal(int, str, str, str)
    # 创建分组的信号
    create_group_singal = pyqtSignal(list, str)
    # 改变好友状态的信号
    change_friend_state_singal = pyqtSignal(str, int, list)
    # 接受未读信息信号
    get_unread_msg_singal = pyqtSignal(list)

    add_friend_singal = pyqtSignal(list)

    add_friend_fail_singal = pyqtSignal(str)

    def setup_ui(self):
        self.setObjectName("MainWindow")
        self.resize(249, 557)
        self.setMinimumSize(QtCore.QSize(249, 557))
        self.setMaximumSize(QtCore.QSize(249, 557))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/logo/chatting1.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet("QMainWindow#MainWindow{background-color:lightblue;}\n"
                           "border-image: url(:/新前缀/QQScLauncher.exe);\n"
                           "background-color: rgb(170, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 512))
        self.centralwidget.setObjectName("centralwidget")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(0, 100, 256, 451))

        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "好友列表")

        self.treeWidget.setIconSize(QSize(50, 50))

        self.lb_head = QtWidgets.QLabel(self.centralwidget)
        self.lb_head.setGeometry(QtCore.QRect(10, 10, 61, 61))
        self.lb_head.setStyleSheet("QLabel#lb_head{border:1px solid gray;}")
        self.lb_head.setText("")
        self.lb_head.setScaledContents(True)
        self.lb_head.setObjectName("lb_head")
        self.lb_name = QtWidgets.QLabel(self.centralwidget)
        self.lb_name.setGeometry(QtCore.QRect(130, 10, 41, 21))
        self.lb_name.setObjectName("lb_name")
        self.lb_id = QtWidgets.QLabel(self.centralwidget)
        self.lb_id.setGeometry(QtCore.QRect(180, 10, 54, 21))
        self.lb_id.setObjectName("lb_id")
        self.lb_email = QtWidgets.QLabel(self.centralwidget)
        self.lb_email.setGeometry(QtCore.QRect(130, 40, 200, 16))
        self.lb_email.setObjectName("lb_email")
        self.tb_add = QtWidgets.QToolButton(self.centralwidget)
        self.tb_add.setGeometry(QtCore.QRect(180, 80, 50, 21))
        self.tb_add.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/list_images/adduser.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tb_add.setIcon(icon1)
        self.tb_add.setIconSize(QtCore.QSize(40, 40))
        self.tb_add.setObjectName("tb_add")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 79, 130, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.setCentralWidget(self.centralwidget)
        self.retranslate_ui()

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "PP 1.0"))
        self.lb_name.setText(_translate("MainWindow", "小强"))
        self.lb_id.setText(_translate("MainWindow", "10001"))
        self.lb_email.setText(_translate("MainWindow", "1001@qq.com"))
        self.tb_add.setText(_translate("MainWindow", "..."))
        # self.tb_search.setText(_translate("MainWindow", "..."))

        self.group = MyGroupWindow(self.treeWidget)
        self.group.isExpanded()


class MyGroupWindow(QtWidgets.QTreeWidgetItem):

    def __init__(self, parent):
        super().__init__(parent)
        # 默认在线的数量为0
        self.onlinenum = 0
        # 默认总好友数为0
        self.allnum = 0
        self.frienddic = {}
        self.setup_ui()

    def setup_ui(self):
        self.set_header()
        self.setIcon(0, QIcon('images/list_images/buddy.ico'))

    def set_header(self):
        self.setText(0, '我的好友 %d/%d' % (self.onlinenum, self.allnum))

    def set_child(self, friend_list, num):
        if num == '1':
            self.allnum = len(friend_list)
        elif num == '0':
            self.allnum += 1
        for i in friend_list:
            # 创建子节点并加入组
            child = FriendView(i['name'], i['friendid'], i['state'], i['head'])
            if i['state'] == '1':
                # 在线数加1
                self.onlinenum += 1
            self.addChild(child)
            self.frienddic[i['friendid']] = child
            # QApplication.processEvents()
        # 设置表头
        self.set_header()

    def change_online_num(self, state):
        if state == '1':
            self.onlinenum += 1
            self.set_header()
        elif state == '0':
            self.onlinenum -= 1
            self.set_header()


class FriendView(QtWidgets.QTreeWidgetItem):

    def __init__(self, name, userid, statecode, head):
        super().__init__()
        self.name = name
        self.userid = userid
        self.state = '离线' if statecode == '0' else '在线'
        self.head = 'images/user/' + head
        self.setup_ui()

    def setup_ui(self):
        '''设置信息'''
        self.setIcon(0, QIcon(self.head))
        msg = '%s (%d)\n%s' % (self.name, self.userid, self.state)
        self.setText(0, msg)

    def set_state(self, statecode):
        '''更新在线状态信息'''
        self.state = '离线' if statecode == '0' else '在线'
        msg = '%s (%d)\n%s' % (self.name, self.userid, self.state)
        self.setText(0, msg)

    def set_info(self, name, head):
        '''更新姓名'''
        self.name = name
        self.head = head
        self.setIcon(0, QIcon(self.head))
        msg = '%s (%d)\n%s' % (self.name, self.userid, self.state)
        self.setText(0, msg)


if __name__ == '__main__':
    app = QApplication([])
    s = BaseMainWindow()
    s.setup_ui()
    s.show()
    import sys
    sys.exit(app.exec_())