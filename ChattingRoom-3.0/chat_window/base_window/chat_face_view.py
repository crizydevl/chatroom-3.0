from PyQt5.QtWidgets import QTableWidget, QDialog, QTableWidgetItem
from PyQt5.QtCore import QRect, Qt, QMetaObject, QSize, QCoreApplication
from PyQt5.QtGui import QFont, QIcon


class BaseChatFaceWindow(QDialog):

    def setup_ui(self):

        self.setWindowTitle('表情')
        # self.setObjectName("表情")
        self.resize(256, 192)
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(QRect(0, 0, 256, 192))
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.DotLine)
        self.tableWidget.setRowCount(6)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(42)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(28)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)

        self.tableWidget.setIconSize(QSize(32, 24))
        self.retranslate_ui()
        QMetaObject.connectSlotsByName(self)

        # 添加表情
        n = 1
        for row in range(6):
            for col in range(6):
                item = QTableWidgetItem()
                item.setTextAlignment(Qt.AlignCenter)
                font = QFont()
                font.setPointSize(1)
                item.setText('images/chatface/' + str(n) + '.gif')
                item.setIcon(QIcon(item.text()))
                self.tableWidget.setItem(row, col, item)
                if n == 35:
                    break
                n += 1

    def retranslate_ui(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.tableWidget.setSortingEnabled(False)


