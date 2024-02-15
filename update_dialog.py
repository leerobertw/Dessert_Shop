import tkinter as tk
from tkinter import simpledialog

class UpdateDialog(simpledialog.Dialog):
    def __init__(self, parent, title, amount=0):
        self.amount = amount
        super().__init__(parent, title)

    def body(self, frame):
        self.member_name = tk.Label(frame, width=25, text="Amount")
        self.member_name.pack()
        self.member_name_box = tk.Entry(frame, width=25)
        if self.amount is not None:
            self.member_name_box.insert(0, str(self.amount))
        self.member_name_box.pack()
        return frame

    def ok_pressed(self):
        self.amount = int(self.member_name_box.get())
        self.destroy()

    def cancel_pressed(self):
        self.destroy()

    def buttonbox(self):
        self.ok_button = tk.Button(self, text='OK', width=5, command=self.ok_pressed)
        self.ok_button.pack(side="left")
        cancel_button = tk.Button(self, text='Cancel', width=5, command=self.cancel_pressed)
        cancel_button.pack(side="right")
        self.bind("<Return>", lambda event: self.ok_pressed())
        self.bind("<Escape>", lambda event: self.cancel_pressed())

class TotalLabel(simpledialog.Dialog):
    def __init__(self, parent, title, total, tax):
        self._total = total
        self._tax = tax
        self.was_ok_pressed = False
        super().__init__(parent, title)

    def body(self, frame):
        total_label = tk.Label(frame, width=25, text=f"your total without tax is, {self._total}")
        total_label.pack()
        tax_label = tk.Label(frame, width=25, text=f"your total tax is, {self._tax}")
        tax_label.pack()
        total_all = tk.Label(frame, width=25, text=f"your total is, {round(self._total + self._tax, 2)}")
        total_all.pack()

    def ok_pressed(self):
        self.was_ok_pressed = True
        self.destroy()

    def cancel_pressed(self):
        self.destroy()

    def buttonbox(self):
        self.ok_button = tk.Button(self, text='OK', width=5, command=self.ok_pressed)
        self.ok_button.pack(side="left")
        cancel_button = tk.Button(self, text='Cancel', width=5, command=self.cancel_pressed)
        cancel_button.pack(side="right")
        self.bind("<Return>", lambda event: self.ok_pressed())
        self.bind("<Escape>", lambda event: self.cancel_pressed())
