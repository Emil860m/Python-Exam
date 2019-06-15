import tkinter
from tkinter import filedialog
from tkinter import Label

import Chat.MVC.View
import Chat.MVC.Model


class chatController:

    def __init__(self):
        """Controller creating the model and the view"""
        self.view = Chat.MVC.View.ClientView(self)
        self.model = Chat.MVC.Model.Client(self)
        self.view.top.mainloop()  # Starts GUI execution.

    def msg_to_send(self, msg):
        """Handles messages going from the view to the model"""
        if isinstance(msg, tkinter.Event) or isinstance(msg, tkinter.StringVar):
            msg = self.view.input.get()
        self.model.send_msg(msg)
        self.view.input.set("")

    def msg_received(self, msg):
        """Handles messages going from the model to the view"""
        if msg.decode().split()[0] == "/file":
            msg = self.receive_file(msg)
        self.view.msg_list.insert(tkinter.END, msg)

    def close(self):
        """Handles what happens when you close the window"""
        self.view.input.set("/quit")
        self.msg_to_send(self.view.input)

    def quit(self):
        """Handles closing the window if you type the /quit command"""
        self.view.top.quit()


    def find_file(self):
        """Finds the file to send to the server"""
        filename = filedialog.askopenfilename(initialdir="/", title="Select file")
        if filename:
            self.model.send_file(filename)

    def receive_file(self, msg):
        """Creates a click-able link to request a file that was send to the server"""
        msg = msg.decode()
        link = Label(self.view.top, text=msg.split()[5], fg="blue", cursor="hand2")
        link.pack()
        link.bind("<Button-1>", lambda e: self.request_file_from_server(link.cget("text")))
        msg = msg.split()[1:]
        return msg


    def request_file_from_server(self, filename):
        """Asks the server to send selected file to the client"""
        self.model.receive_file(filename)
