import tkinter

import MVC.View
import MVC.Model

class ChatController:

    def __init__(self):
        self.model = MVC.Model.Client(self)
        self.view = MVC.View.ChatView(self)

    def msg(self, msg):
        return msg

    def receive(self, msg):
        self.view.msg_list.insert(tkinter.END, msg)

    def send(self, msg):
        self.model.send(msg)

    def on_closing(self):
        """This function is to be called when the window is closed."""
        self.send("{quit}")
        self.model.alive = 0