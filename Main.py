# Import packages
import customtkinter
import tkinter
from tkinter import font

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry(f"{720}x{980}")
custom_font = font.Font(family="typewrite", size=70, weight="normal")


def login_page():
    after_frame.pack_forget()
    login_frame.pack()


def after_page():
    login_frame.pack_forget()
    after_frame.pack()


# page 1
login_frame = customtkinter.CTkFrame(master=root)
login_frame.pack(pady=20, padx=60, fill="both", expand=True)

label = tkinter.Label(master=login_frame, text="Login", font=custom_font, fg="#1f538d",
                           bg="#212121")
label.pack(pady=120, padx=10)

entry_1 = customtkinter.CTkEntry(master=login_frame, placeholder_text="Username", width=300, height=30
                                      )
entry_1.pack(pady=12, padx=10)

entry_2 = customtkinter.CTkEntry(master=login_frame, placeholder_text="Password", show="*", width=300,
                                      height=30)
entry_2.pack(pady=30, padx=10)

button = customtkinter.CTkButton(master=login_frame, text="Login", command=after_page)
button.pack(pady=30, padx=10)

checkbox = customtkinter.CTkCheckBox(master=login_frame, text="Remember Me")
checkbox.pack(pady=160, padx=10)

# page 2
after_frame = customtkinter.CTkFrame(master=root)
after_frame.pack(pady=20, padx=60, fill="both", expand=True)

label = tkinter.Label(master=after_frame, text="you logged in", font=custom_font, fg="#1f538d",
                           bg="#212121")
label.pack(pady=120, padx=10)

button = customtkinter.CTkButton(master=after_frame, text="back", command=login_page)
button.pack(pady=30, padx=10)

login_page()

root.mainloop()
