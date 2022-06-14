from tkinter import *
from cryption import *
import apps
import time

root = Tk()
root.title("Password Manager")
root.geometry("500x250")
root.resizable(False, False)

def main(user):
	for widget in root.winfo_children():
		widget.destroy()
	Label (root, text=f"Hello {user}!", font=('arial', 25)).place(x=165, y=10)	
	Button(root, text="Passwords", font=('arial', 19), command=lambda:apps.passwords(root)).place(x=35, y=75,  height=40, width=150)
	Button(root, text="Cards", font=('arial', 20), command=lambda:apps.cards(root)).place(x=35, y=130, height=40, width=150)
	Button(root, text="Change Password", font=('arial', 12), command=lambda:apps.changePass(root)).place(x=35, y=185, height=40, width=150)
	Button(root, text="Crypto Vault", font=('arial', 16), command=lambda:apps.vault(root)).place(x=205, y=75, height=40, width=150)
	Button(root, text="Notes", font=('arial', 20), command=lambda:apps.notes(root)).place(x=205, y=130, height=40, width=150)

def login():
	passwd = encryptpsw(passwordEntry.get())
	with open('files/login.txt', 'r') as f:
		pwd = f.read().split(',')
	if passwd == pwd[0].strip('\n'):
		main(pwd[1].strip('\n'))
	else:
		Label(root, text="Wrong Password", font=('arial', 20)).place(x=20, y=210)

Label(root, text="Welcome Back", font=('arial', 20)).place(x=160, y=40)
Label(root, text="Please Login", font=('arial', 20)).place(x=175, y=70)
passwordEntry = Entry(root, font=('arial', 18), justify="center")
passwordEntry.place(x=150, y=120, height=30, width=200)
Button(root, text="Login", font=('arial', 18), command=login).place(x=150, y=165, height=30, width=200)

root.mainloop()
