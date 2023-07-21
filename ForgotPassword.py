import tkinter as tk
from tkinter import font
from tkinter import *
from PIL import ImageTk, Image

class ForgotPasswordPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('720x980')
        self.title('Forgot Password')
        self.custom_font = font.Font(family="typewriter", size=60, weight="normal")
        self.initialize_widgets()

    def initialize_widgets(self):
        self.bg_image = ImageTk.PhotoImage(Image.open("Login page/another one.png"))
        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(y=0, x=0)

        reset_password_title = tk.Label(self, text='Reset Password', font=self.custom_font, bg='white', fg='#0d2158')
        reset_password_title.place(y=140, x=70)

        email_label = tk.Label(self, text='Email:', font=("typewriter", 15, "normal"), bg='white', fg='#0d2158')
        email_label.place(y=355, x=150)

        self.email_entry = tk.Entry(self, font=("typewriter", 20, "normal"), fg="white", bg='#0d2158', width=30)
        self.email_entry.place(y=385, x=150)

        reset_password_explanation = tk.Label(self,
                                              text='Enter your email and you will be sent a link shortly to reset'
                                                   ' your\n password',
                                              font=("typewriter", 15, "normal"),
                                              bg='white', fg='firebrick1')
        reset_password_explanation.place(y=230, x=100)

        self.reset_password_button = tk.Button(self,
                                               text="Reset Password",
                                               font=("typewriter", 20, "bold"),
                                               bd=0,
                                               bg='#0d2158',
                                               activebackground='#0d2158',
                                               cursor='hand2',
                                               fg="white",
                                               width=19)
        self.reset_password_button.place(x=215, y=580)

if __name__ == "__main__":
    forgot_password_page = ForgotPasswordPage()
    forgot_password_page.mainloop()