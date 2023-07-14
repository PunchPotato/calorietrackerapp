import tkinter as tk
from tkinter import font
from tkinter import *
from PIL import ImageTk, Image


class SignupPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('720x980')
        self.title('Sign Up')
        self.custom_font = font.Font(family="typewriter", size=45, weight="normal")
        self.open_eye = None
        self.close_eye = None
        self.initialize_widgets()

    def initialize_widgets(self):
        self.bg_image = ImageTk.PhotoImage(Image.open("Login page/trial 2.png"))
        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(y=0, x=0)

        create_account_title = tk.Label(self, text='CREATE AN ACCOUNT', font=self.custom_font, bg='white', fg='#0d2158')
        create_account_title.place(y=200, x=30)

        email_title = tk.Label(self, text='Email:', font=("typewriter", 15, "normal"), bg='white', fg='#0d2158')
        email_title.place(y=295, x=150)

        self.email_entry = tk.Entry(self, font=("typewriter", 20, "normal"), fg="white", bg='#0d2158', width=30)
        self.email_entry.place(y=325, x=150)
        self.email_entry.bind("<FocusIn>", self.temp_name_entry_text)

        username_title = tk.Label(self, text='Username:', font=("typewriter", 15, "normal"), bg='white', fg='#0d2158')
        username_title.place(y=395, x=150)

        self.username_entry = tk.Entry(self, font=("typewriter", 20, "normal"), fg="white", bg='#0d2158', width=30)
        self.username_entry.place(y=425, x=150)
        self.username_entry.bind("<FocusIn>", self.temp_name_entry_text)

        password_title = tk.Label(self, text='Password:', font=("typewriter", 15, "normal"), bg='white', fg='#0d2158')
        password_title.place(y=495, x=150)

        self.password_entry = tk.Entry(self, font=("typewriter", 20, "normal"), fg="white", bg='#0d2158', width=30)
        self.password_entry.place(y=525, x=150)
        self.password_entry.bind("<FocusIn>", self.temp_password_entry_text)

        confirm_password_title = tk.Label(self, text='Password:', font=("typewriter", 15, "normal"), bg='white', fg='#0d2158')
        confirm_password_title.place(y=595, x=150)

        self.password_comfirm_entry = tk.Entry(self, font=("typewriter", 20, "normal"), fg="white", bg='#0d2158', width=30)
        self.password_comfirm_entry.place(y=625, x=150)
        self.password_comfirm_entry.bind("<FocusIn>", self.temp_password_entry_text)

        create_account_button = tk.Button(self, text="Create Account", font=("typewriter", 20, "bold"), bd=0,
                                          bg='#0d2158',activebackground='#0d2158', cursor='hand2', fg="white", width=19)
        create_account_button.place(y=700, x=210)

        self.signupLabel = Label(self, text="Or...", font=('Open Sans', 9), fg='firebrick1',
                                 bg='white')
        self.signupLabel.place(x=335, y=760)

        self.newaccountButton = Button(self, text='Log In', font=('Open Sans', 9, 'bold underline'),
                                       fg='blue', bg='white', activeforeground='blue', activebackground='white',
                                       cursor='hand2', bd=0, command=self.signup_page)
        self.newaccountButton.place(x=360, y=760)


    def temp_name_entry_text(self, event):
        self.email_entry.delete(0, "end")

    def temp_password_entry_text(self, event):
        self.password_entry.delete(0, "end")

    def signup_page(self):
        Sign_up_page.destroy()
        import Login
        Login.LoginPage().mainloop()



if __name__ == "__main__":
    Sign_up_page = SignupPage()
    Sign_up_page.mainloop()
