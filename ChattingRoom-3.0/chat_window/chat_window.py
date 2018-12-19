import json
import re
import datetime
import traceback
from .base_window.chat_view import BaseChatWindow
from .chat_face_window import ChatFaceWindow


class ChatWindow(BaseChatWindow):

    def __init__(self, parent, tcp, udp, name, addr, frienid, myid, state):
        super().__init__(parent)
        self.tcp = tcp
        self.udp = udp
        self.name = name
        self.state = state
        self.addr = tuple(addr)
        self.id = frienid
        self.myid = myid
        self.setup_ui()
        self.connect_func()
        self.setWindowTitle('与' + self.name + '聊天中..')

    @staticmethod
    def json_encode_msg(content):
        return json.dumps(content).encode('utf-8')

    def connect_func(self):
        # chatface
        self.toolButton_4.clicked.connect(self.face_window)
        # @
        self.toolColorBtn.clicked.connect(lambda x: print('11111111111111'))
        # clear
        self.toolButton_2.clicked.connect(self.clear_msg)
        # 星星
        self.toolButton_3.clicked.connect(lambda x: print('333333333333333333'))
        # 发送按钮
        self.pushButton.clicked.connect(self.send_msg)

    def face_window(self):
        chat_face = ChatFaceWindow(self)
        chat_face.show()

    def send_msg(self):
        # html文本的聊天框信息内容
        try:
            html_msg = self.textEdit.toHtml()
            # 获取时间
            time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # 显示在聊天窗口的上方聊天框
            self.my_msg_show_in_chat_window(html_msg, time)
            # 发送给好友和服务器
            self.send_to_friend_and_server(html_msg, time)
            # 发送完毕后清除输入框的内容
            self.textEdit.clear()
        except:
            traceback.print_exc()

    def my_msg_show_in_chat_window(self, content, time):
        content = re.sub(r'<p', '<p style="color:red">%s %s</p><p', content, re.S)
        self.textBrowser.append(content % ('我', time))

    @staticmethod
    def parse_send_content(content):
        '''解析发送内容，去掉多余的html标签'''
        # 得到p标签里的内容
        p_content = re.search(r'<p style.*?>(.*)</p>', content, re.S).group(1)
        # 格式化img标签
        send_content = re.sub(r'<img src="images/chatface/', '<img"', p_content)
        return send_content

    @staticmethod
    def parse_recv_content(content):
        # 还原img标签
        if re.findall(r'<img.*?>', content):
            content = re.sub(r'<img"', '<img src="images/chatface/', content)
        # 加上其他html标签
        html = '''<html><head><meta name="qrichtext" content="1" /><style type="text/css">
                    p, li { white-space: pre-wrap; }
                    </style></head><body style=" font-family:'SimSun'; font-size:9pt; 
                    font-weight:400; font-style:normal;">
                    <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; 
                    margin-right:0px; -qt-block-indent:0; text-indent:0px;">%s</p>
                    </body>
                    </html>'''
        return html % content

    def send_to_friend_and_server(self, content, time):
        '''向服务器和好友发送聊天信息'''
        print('friendaddr', self.addr)
        try:
            send_content = self.parse_send_content(content)
            tcp_msg = self.json_encode_msg({'T': 'SC', 'friendid': self.id, 'content': send_content, 'time': time})
            udp_msg = self.json_encode_msg({'T': 'SC', 'friendid': self.myid, 'content': send_content, 'time': time})
            self.tcp.send(tcp_msg)
            if self.state == '1':
                self.udp.sendto(udp_msg, self.addr)

        except Exception:
            traceback.print_exc()

    def get_new_msg(self, content, time):
        '''处理新消息的方法'''
        content = self.parse_recv_content(content)
        self.friend_msg_show_in_chat_window(content, time)

    def friend_msg_show_in_chat_window(self, content, time):
        '''朋友发来的信息显示在窗口上'''
        content = re.sub(r'<p', '<p style="color:green">%s %s</p><p', content, re.S)
        self.textBrowser.append(content % (self.name, time))

    def clear_msg(self):
        '''清除聊天信息'''
        self.textEdit.clear()