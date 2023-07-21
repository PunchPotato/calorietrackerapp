import tkinter as tk
from tkinter import font
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql


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
                                               width=19,
                                               command=self.connect_to_email)
        self.reset_password_button.place(x=215, y=580)

        self.login_lable = Label(self, text="Now...", font=('Open Sans', 9), fg='firebrick1',
                                 bg='white')
        self.login_lable.place(x=325, y=680)

        self.login_button = Button(self, text='Log In', font=('Open Sans', 9, 'bold underline'),
                                       fg='blue', bg='white', activeforeground='blue', activebackground='white',
                                       cursor='hand2', bd=0, command=self.login_page)
        self.login_button.place(x=360, y=680)

    def login_page(self):
        self.destroy()
        import Login
        Login.LoginPage().mainloop()


    def connect_to_email(self):
        email = self.email_entry.get().strip()

        if email == '':
            messagebox.showerror("Error", "All fields must be filled.")
            return

        con = None
        my_cursor = None
        try:
            con = pymysql.connect(host='localhost', user='root', password='*****************',
                                  database='mydatabase')
            my_cursor = con.cursor()

            query = 'SELECT * FROM user_data WHERE email = %s'
            my_cursor.execute(query, (email,))
            row = my_cursor.fetchone()

            if row is None:
                messagebox.showerror('Error', 'Email is not valid')
            else:
                messagebox.showinfo('Success', 'Email has been sent.')

        except pymysql.Error as e:
            messagebox.showerror("Error", "Failed to connect to the database: " + str(e))

        finally:
            try:
                if my_cursor is not None:
                    my_cursor.close()
                if con is not None:
                    con.close()
            except pymysql.Error:
                pass


if __name__ == "__main__":
    forgot_password_page = ForgotPasswordPage()
    forgot_password_page.mainloop()
    
