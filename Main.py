import tkinter as tk
from tkinter import font
from tkinter import *
from PIL import ImageTk, Image


class LoginPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('720x980')
        self.title('Login Page')
        self.custom_font = font.Font(family="typewriter", size=70, weight="normal")
        self.open_eye = None
        self.close_eye = None
        self.initialize_widgets()

    def initialize_widgets(self):
        self.bg_image = ImageTk.PhotoImage(Image.open("Login page/trial 2.png"))
        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(y=0, x=0)

        login_title = tk.Label(self, text='USER LOGIN', font=self.custom_font, bg='white', fg='#0d2158')
        login_title.place(y=200, x=60)

        self.name_entry = tk.Entry(self, font=("typewrite", 20, "normal"), fg="grey", bd=0)
        self.name_entry.insert(0, "Username")
        self.name_entry.place(y=350, x=220)
        self.name_entry.bind("<FocusIn>", self.temp_name_entry_text)

        self.password_entry = tk.Entry(self, font=("typewrite", 20, "normal"), fg="grey", bd=0)
        self.password_entry.insert(0, "Password")
        self.password_entry.place(y=450, x=220)
        self.password_entry.bind("<FocusIn>", self.temp_password_entry_text)

        self.open_eye = ImageTk.PhotoImage(Image.open('Login page/openeye.png'))
        self.close_eye = ImageTk.PhotoImage(Image.open('Login page/closeeye.png'))
        self.eye_button = Button(self, image=self.open_eye, bd=0, bg='white', activebackground='white', cursor='hand2',
                                 command=self.hide)
        self.eye_button.place(y=450, x=500)

        self.forget_button = Button(self, text='Forgot Password?', bd=0, bg='white', activebackground='white',
                                    cursor='hand2', font=("typewrite", 9, "bold"), fg='firebrick1',
                                    activeforeground='firebrick1')
        self.forget_button.place(x=410, y=495)

        tk.Frame(self, width=300, height=2, bg="#0d2158").place(y=390, x=220)
        tk.Frame(self, width=300, height=2, bg="#0d2158").place(y=490, x=220)

        login_button = tk.Button(self, text="Log in", font=("typewrite", 20, "bold"),  bd=0, bg='#0d2158',
                                 activebackground='#0d2158', cursor='hand2', fg="white", width=19)
        login_button.place(y=550, x=210)

        or_label = Label(self, text='----------------------------OR----------------------------', font=("typewrite", 20)
                         , fg='#0d2158', bg='white')
        or_label.place(x=100, y=620)

    def temp_name_entry_text(self, event):
        self.name_entry.delete(0, "end")

    def temp_password_entry_text(self, event):
        self.password_entry.delete(0, "end")

    def hide(self):
        self.password_entry.config(show='*')
        self.eye_button.config(image=self.close_eye, command=self.show)

    def show(self):
        self.password_entry.config(show='')
        self.eye_button.config(image=self.open_eye, command=self.hide)


if __name__ == "__main__":
    login_page = LoginPage()
    login_page.mainloop()

