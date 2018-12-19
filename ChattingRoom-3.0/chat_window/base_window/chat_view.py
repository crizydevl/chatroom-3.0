from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent, QTextCursor
from PyQt5.QtWidgets import QDialog


class MyTextEdit(QtWidgets.QTextEdit):
    '''自定义TextEdit输入框类，用于自定义enter和return事件'''

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def keyPressEvent(self, event):
        keyevent = QKeyEvent(event)
        if keyevent.key() in (Qt.Key_Enter, Qt.Key_Return):
            self.parent.pushButton.clicked.emit()
        else:
            # 按键不是enter时使用父类的keyPressEvent
            super().keyPressEvent(event)


class BaseChatWindow(QDialog):

    def setup_ui(self):

        self.setObjectName("Dialog")
        self.resize(512, 466)

        self.textBrowser = QtWidgets.QTextBrowser(self)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.moveCursor(QTextCursor.End)

        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 7)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 2, 1, 1)
        self.toolButton_4 = QtWidgets.QToolButton(self)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/chat/face1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_4.setIcon(icon)
        self.toolButton_4.setObjectName("toolButton_4")
        self.gridLayout.addWidget(self.toolButton_4, 1, 3, 1, 1)
        self.toolButton_3 = QtWidgets.QToolButton(self)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/chat/italic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon1)
        self.toolButton_3.setObjectName("toolButton_3")
        self.gridLayout.addWidget(self.toolButton_3, 1, 4, 1, 1)
        self.toolButton_2 = QtWidgets.QToolButton(self)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/chat/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon2)
        self.toolButton_2.setObjectName("toolButton_2")
        self.gridLayout.addWidget(self.toolButton_2, 1, 5, 1, 1)
        self.toolColorBtn = QtWidgets.QToolButton(self)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/chat/color.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolColorBtn.setIcon(icon3)
        self.toolColorBtn.setObjectName("toolColorBtn")
        self.gridLayout.addWidget(self.toolColorBtn, 1, 6, 1, 1)
        # self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit = MyTextEdit(self)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 2, 0, 1, 7)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 1)

        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        # self.setWindowTitle(_translate("self", "self"))
        self.toolButton_4.setText(_translate("self", "..."))
        self.toolButton_3.setText(_translate("self", "..."))
        self.toolButton_2.setText(_translate("self", "..."))
        self.toolColorBtn.setText(_translate("self", "..."))
        self.pushButton.setText(_translate("self", "发送>>"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#
#     ui = Ui_Dialog()
#     ui.setupUi(self)
#     ui.show()
#     sys.exit(app.exec_())

