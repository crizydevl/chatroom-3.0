from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QDialog, QLineEdit


class BaseRegisterDialog(QDialog):

    # 注册成功发送的信号
    regist_s = pyqtSignal(int)

    def setupUi(self):

        self.setObjectName("Dialog")
        self.setWindowModality(QtCore.Qt.NonModal)
        self.resize(284, 310)
        self.setMinimumSize(QtCore.QSize(284, 310))
        self.setMaximumSize(QtCore.QSize(284, 310))
        self.setStyleSheet("background-image: url(images/logo/chatting1.ico);")
        # 姓名
        self.lineEdit_6 = QtWidgets.QLineEdit(self)
        self.lineEdit_6.setGeometry(QtCore.QRect(90, 10, 131, 20))
        self.lineEdit_6.setObjectName("lineEdit_pwd")
        self.lineEdit_6.setPlaceholderText("昵称")
        # 年龄
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(90, 48, 131, 20))
        self.lineEdit.setObjectName("lineEdit_name")
        self.lineEdit.setPlaceholderText("年龄")
        # 密码
        self.lineEdit_3 = QtWidgets.QLineEdit(self)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 86, 131, 20))
        self.lineEdit_3.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit_3.setEchoMode(QLineEdit.Password)
        self.lineEdit_3.setPlaceholderText("密码6~15位，由字母、数字组成")
        self.lineEdit_3.setObjectName("lineEdit_pwd")
        # 再次输入密码
        self.lineEdit_7 = QtWidgets.QLineEdit(self)
        self.lineEdit_7.setGeometry(QtCore.QRect(90, 124, 131, 20))
        self.lineEdit_7.setObjectName("lineEdit_pwd2")
        self.lineEdit_7.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit_7.setEchoMode(QLineEdit.Password)
        self.lineEdit_7.setPlaceholderText("密码6~15位，由字母、数字组成")
        # 邮箱
        self.lineEdit_4 = QtWidgets.QLineEdit(self)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 162, 131, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(30, 48, 54, 21))
        self.label_4.setObjectName("lb_name")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(30, 86, 54, 21))
        self.label_5.setObjectName("lb_pwd_2")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(30, 124, 91, 21))
        self.label_2.setObjectName("lb_pwd")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(30, 162, 54, 21))
        self.label_3.setObjectName("lb_email")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(30, 10, 54, 20))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(8)

        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(220, 122, 54, 20))
        self.label_6.setObjectName("lb_pwd2")
        # 邮箱验证码
        self.lineEdit_5 = QtWidgets.QLineEdit(self)
        self.lineEdit_5.setGeometry(QtCore.QRect(90, 233, 100, 20))
        self.lineEdit_5.setObjectName("lineEdit_core")
        self.radioButton = QtWidgets.QRadioButton(self)
        self.radioButton.setGeometry(QtCore.QRect(90, 200, 89, 16))
        self.radioButton.setObjectName("radioButton_man")
        self.radioButton_2 = QtWidgets.QRadioButton(self)
        self.radioButton_2.setGeometry(QtCore.QRect(190, 200, 89, 16))
        self.radioButton_2.setObjectName("radioButton_wuman")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 233, 75, 20))
        self.pushButton_2.setObjectName("pushButton_core")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(90, 270, 100, 30))
        self.pushButton.setObjectName("pushButton_zhuce")

        self.setWindowIcon(QIcon('images/logo/chatting1.ico'))



        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "注册"))
        self.label.setText(_translate("self", "昵   称"))
        self.label_5.setText(_translate("self", "密  码"))
        self.label_3.setText(_translate("self", "邮   箱"))
        self.radioButton.setText(_translate("self", "男"))
        self.label_4.setText(_translate("self", "年   龄"))
        self.pushButton.setText(_translate("self", "注册>>"))
        self.label_2.setText(_translate("self", "再次输入"))
        self.pushButton_2.setText(_translate("self", "邮箱验证码"))
        self.radioButton_2.setText(_translate("self", "女"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = BaseRegisterDialog()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
