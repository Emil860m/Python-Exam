import tkinter

class ChatView:

    def __init__(self, controller):

        self.controller = controller

        top = tkinter.Tk()
        top.title("Chatter")

        messages_frame = tkinter.Frame(top)
        my_msg = tkinter.StringVar()  # For the messages to be sent.
        my_msg.set("")
        scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
        # Following will contain the messages.

        self.msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
        self.msg_list.pack()
        messages_frame.pack()

        entry_field = tkinter.Entry(top, textvariable=my_msg)
        entry_field.bind("<Return>", controller.msg(my_msg))
        entry_field.pack()
        send_button = tkinter.Button(top, text="Send", command=controller.msg(my_msg))
        send_button.pack()

        top.protocol("WM_DELETE_WINDOW", controller.on_closing)

        tkinter.mainloop()  # Starts GUI execution.