import tkinter


class ClientView:

    def __init__(self, controller):
        """Handles the view, creating a window with received messages, input field and a send button"""
        self.controller = controller

        self.top = tkinter.Tk()
        self.top.title("Chatter")

        self.input = tkinter.StringVar()  # For the messages to be sent.
        self.input.set("")

        """Message box"""
        messages_frame = tkinter.Frame(self.top)
        scrollbar = tkinter.Scrollbar(messages_frame)
        self.msg_list = tkinter.Listbox(messages_frame, height=15, width=60, yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
        self.msg_list.pack()
        messages_frame.pack()




        """Input box and send button"""
        entry_field = tkinter.Entry(self.top, textvariable=self.input)
        entry_field.bind("<Return>", self.controller.msg_to_send)
        entry_field.pack()
        send_button = tkinter.Button(self.top, text="Send", command=lambda: self.controller.msg_to_send(self.input))
        send_button.pack()
        """Send file button"""
        file_button = tkinter.Button(self.top, text="Send file", command=lambda: self.controller.find_file())
        file_button.pack()

        """On closing the window"""
        self.top.protocol("WM_DELETE_WINDOW", self.controller.close)
