import sys
from PyQt5.QtWidgets import QApplication
from client import Client, MyThread

app = QApplication(sys.argv)
client = Client()
t = MyThread(client)
t.start()
try:
    app.exec_()
    sys.exit(app.exec_())
except Exception:
    sys.exit()
finally:
    client.tell_friend_offline()

