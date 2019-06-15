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
            msg = self.view.input.get()
        self.model.send_msg(msg)
        self.view.input.set("")

    def msg_received(self, msg):
        """Handles messages going from the model to the view"""
        self.view.msg_list.insert(tkinter.END, msg)

    def close(self):
        """Handles what happens when you close the window"""
        self.view.input.set("/quit")
        self.msg_to_send(self.view.input)

    def quit(self):
        """Handles closing the window if you type the /quit command"""
        self.view.top.quit()

    """Not working yet"""
    def find_file(self):
        """Finds the file to send to the server"""
        filename = self.view.top.filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        self.msg_to_send("/file")
        self.model.send_file(filename)

