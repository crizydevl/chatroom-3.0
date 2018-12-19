from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication


class Add_friend_Dialog(QDialog):
    def setup_ui(self):
        self.setObjectName("Dialog")
        self.resize(200, 100)
        icon = QtGui.QIcon()
        import os
        print('地址', os.getcwd())
        icon.addPixmap(QtGui.QPixmap("App/Views/images/logo/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setSizeGripEnabled(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 9, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_add = QtWidgets.QLineEdit(self)
        self.lineEdit_add.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit_add)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        # self.label_3 = QtWidgets.QLabel(self)
        # self.label_3.setObjectName("label_3")
        # self.horizontalLayout_3.addWidget(self.label_3)
        # self.comboBox = QtWidgets.QComboBox(self)
        # self.comboBox.setObjectName("comboBox")
        # self.horizontalLayout_3.addWidget(self.comboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "添增联系人"))
        self.setWhatsThis(_translate("self", "新增联系人"))
        self.label.setText(_translate("self", "联系人帐号"))
        # self.label_3.setText(_translate("self", "联系人分组"))


if __name__ == '__main__':
    app = QApplication([])
    s = Add_friend_Dialog()
    s.setup_ui()
    s.show()
    import sys
    sys.exit(app.exec_())