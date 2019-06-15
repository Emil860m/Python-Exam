from tkinter import filedialog
import tkinter
from tkinter import *
def find_file(root):
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    print(root.filename)

root = Tk()
root.filename = ""
send_button = tkinter.Button(root, text="Send", command=lambda: find_file(root))
send_button.pack()



root.mainloop()