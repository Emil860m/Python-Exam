import tkinter


class ClientView:

    def __init__(self, controller):
        """Handles the view, creating a window with received messages, input field and a send button"""
        self.controller = controller

        self.top = tkinter.Tk()
        self.top.title("Chatter")

        messages_frame = tkinter.Frame(self.top)
        self.my_msg = tkinter.StringVar()  # For the messages to be sent.
        self.my_msg.set("")
        scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
        # Following will contain the messages.
        self.msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
        self.msg_list.pack()
        messages_frame.pack()

        entry_field = tkinter.Entry(self.top, textvariable=self.my_msg)
        entry_field.bind("<Return>", self.controller.msg_to_send)
        entry_field.pack()
        send_button = tkinter.Button(self.top, text="Send", command=lambda: self.controller.msg_to_send(self.my_msg))
        send_button.pack()

        self.top.protocol("WM_DELETE_WINDOW", self.controller.close)
