import tkinter as tk
from tkinter import font
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql


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

        username_title = tk.Label(self, text='Username:', font=("typewriter", 15, "normal"), bg='white', fg='#0d2158')
        username_title.place(y=395, x=150)

        self.username_entry = tk.Entry(self, font=("typewriter", 20, "normal"), fg="white", bg='#0d2158', width=30)
        self.username_entry.place(y=425, x=150)

        password_title = tk.Label(self, text='Password:', font=("typewriter", 15, "normal"), bg='white', fg='#0d2158')
        password_title.place(y=495, x=150)

        self.password_entry = tk.Entry(self, font=("typewriter", 20, "normal"), fg="white", bg='#0d2158', width=30)
        self.password_entry.place(y=525, x=150)

        confirm_password_title = tk.Label(self, text='Comfirm Password:', font=("typewriter", 15, "normal"), bg='white',
                                          fg='#0d2158')
        confirm_password_title.place(y=595, x=150)

        self.password_comfirm_entry = tk.Entry(self, font=("typewriter", 20, "normal"), fg="white", bg='#0d2158',
                                               width=30)
        self.password_comfirm_entry.place(y=625, x=150)

        create_account_button = tk.Button(self, text="Create Account", font=("typewriter", 20, "bold"), bd=0,
                                          bg='#0d2158', activebackground='#0d2158', cursor='hand2', fg="white",
                                          width=19, command=self.connect_database)
        create_account_button.place(y=700, x=210)

        self.terms_and_conditions_label= Label(self, text="I agree to Terms & Conditions", font=('Open Sans', 12),
                                               fg='firebrick1', bg='white')
        self.terms_and_conditions_label.place(x=270, y=665)

        self.check = IntVar()
        terms_and_conditions_box = tk.Checkbutton(self, bd=0, bg='white', variable=self.check)
        terms_and_conditions_box.place(x=245, y=665)

        self.signupLabel = Label(self, text="Or...", font=('Open Sans', 9), fg='firebrick1',
                                 bg='white')
        self.signupLabel.place(x=335, y=760)

        self.newaccountButton = Button(self, text='Log In', font=('Open Sans', 9, 'bold underline'),
                                       fg='blue', bg='white', activeforeground='blue', activebackground='white',
                                       cursor='hand2', bd=0, command=self.signup_page)
        self.newaccountButton.place(x=360, y=760)

    def clear(self):
        self.email_entry.delete(0, END)
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.password_comfirm_entry.delete(0, END)
        self.check.set(0)


    def signup_page(self):
        self.destroy()
        import Login
        Login.LoginPage().mainloop()

    def create_account(self):
        try:
            con = pymysql.connect(host='localhost', user='root', password='****************')
            my_cursor = con.cursor()
            query = 'create database if not exists mydatabase'
            my_cursor.execute(query)
            query = 'use mydatabase'
            my_cursor.execute(query)
            query = 'create table if not exists user_data(id int auto_increment primary key not null, ' \
                    'email varchar(50), username varchar(100), password varchar(20))'
            my_cursor.execute(query)
            con.commit()

            query = 'select * from user_data where username =%s'
            my_cursor.execute(query, (self.username_entry.get()))

            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "username already exists.")
            else:
                query = 'insert into user_data (email, username, password) values(%s, %s, %s)'
                my_cursor.execute(query, (self.email_entry.get(), self.username_entry.get(), self.password_entry.get()))

                con.commit()
                con.close()

                messagebox.showinfo("Success", "Account created successfully!")
                self.clear()
                self.destroy()
                import Login
                Login.LoginPage().mainloop()

        except pymysql.Error as e:
            messagebox.showerror("Error", f"Failed to connect to the database. Error: {str(e)}")
            return

    def connect_database(self):
        if self.email_entry.get() == '' or self.username_entry.get() == '' or self.password_entry.get() == '' or\
                self.password_comfirm_entry.get() == '':
            messagebox.showerror("Error", "All fields must be filled.")
        elif self.password_comfirm_entry.get() != self.password_comfirm_entry.get():
            messagebox.showerror("Error", "Passwords do not match.")
        elif self.check.get() == 0:
            messagebox.showerror("Error", "Accept Terms & Conditions.")
        else:
            self.create_account()


if __name__ == "__main__":
    Sign_up_page = SignupPage()
    Sign_up_page.mainloop()
