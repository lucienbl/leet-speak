from tkinter import *
from src.LeetHelper import LeetHelper


class UiHelper:
    def __init__(self):
        self.window = Tk()
        self.text = StringVar()
        self.response_label = Label(self.window, text="Please enter a string")
        self.leetHelper = LeetHelper()

    def createWindow(self):
        self.window.title("Leet Speak")
        self.window.geometry("300x150")

    def createForm(self):
        assert self.window

        self.text.set("")
        text_input = Entry(self.window, textvariable=self.text, width=20)
        text_input.pack()

        encode_btn = Button(self.window, text="Encode", command=self.encode_string)
        encode_btn.pack(side=BOTTOM)

        decode_btn = Button(self.window, text="Decode", command=self.decode_string)
        decode_btn.pack(side=BOTTOM)

        self.response_label.pack(side=TOP)

    def encode_string(self):
        encoded_string = self.leetHelper.encode(self.text.get(), 0)
        self.response_label.config(text=encoded_string)

    def decode_string(self):
        encoded_string = self.leetHelper.decode(self.text.get())
        self.response_label.config(text=encoded_string)

    def start(self):
        self.window.mainloop()
