from .base_window.chat_face_view import BaseChatFaceWindow


class ChatFaceWindow(BaseChatFaceWindow):

    def __init__(self, parent):
        super().__init__(parent)
        self.setup_ui()
        self.connect_func()

    def connect_func(self):
        self.tableWidget.clicked.connect(self.get_chat_face)

    def get_chat_face(self):
        hititem = self.tableWidget.currentItem()
        print(hititem.text())
        self.tableWidget.parent().parent().textEdit.insertHtml('<img src="%s">' % hititem.text())
        self.close()
