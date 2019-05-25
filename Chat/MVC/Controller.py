import tkinter

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
            msg = self.view.my_msg.get()
        self.model.send_msg(msg)
        self.view.my_msg.set("")

    def msg_received(self, msg):
        """Handles messages going from the model to the view"""
        self.view.msg_list.insert(tkinter.END, msg)

    def close(self):
        """Handles what happens when you close the window"""
        self.view.my_msg.set("{quit}")
        self.msg_to_send(self.view.my_msg)

    def quit(self):
        """Handles closing the window if you type the {quit} command"""
        self.view.top.quit()
