from tkinter import *
from cryption import encryptpsw, make_key
import apps
import time
import os

root = Tk()
root.title("Password Manager")
root.geometry("525x250")
root.resizable(False, False)

def main(user):
	
	for widget in root.winfo_children():
		widget.destroy()

	def get_time():
		timeVar = time.strftime("%I:%M %p")
		dayVar = time.strftime("%m/%d")
		dateDay.config(text=dayVar)
		dateTime.config(text=timeVar)
		dateTime.after(1000, get_time)

	dateTime = Label(root, text="", font=('arial', 15))
	dateTime.place(x=420, y=5)
	dateDay = Label(root, text="", font=('arial', 15))
	dateDay.place(x=10, y=5)
	get_time()

	Label (root, text=f"Hello {user}!",  font=('arial', 25)).place(x=165, y=10)	
	Button(root, text="Passwords",       font=('arial', 19), command=lambda:apps.passwords(root, user)  ).place(x=20, y=75,   height=40, width=150)
	Button(root, text="Cards",           font=('arial', 20), command=lambda:apps.cards(root, user)      ).place(x=20, y=130,  height=40, width=150)
	Button(root, text="Crypto Vault",    font=('arial', 16), command=lambda:apps.vault(root, user)      ).place(x=20, y=185,  height=40, width=150)
	Button(root, text="Notes",           font=('arial', 20), command=lambda:apps.notes(root, user)      ).place(x=190, y=75, height=40, width=150)
	Button(root, text="Log Out",         font=('arial', 16), command=login).place(x=360, y=75, height=40, width=150)
	Button(root, text="Delete Account",  font=('arial', 14), command=lambda:apps.delete(root, user)).place(x=360, y=130, height=40, width=150)
	Button(root, text="Change Password", font=('arial', 12), command=lambda:apps.changePass(root, user) ).place(x=360, y=185,  height=40, width=150)

def login():
	for widget in root.winfo_children():
		widget.destroy()

	def get_time():
		timeVar = time.strftime("%I:%M %p")
		dayVar = time.strftime("%m/%d")
		dateDay.config(text=dayVar)
		dateTime.config(text=timeVar)
		dateTime.after(1000, get_time)

	def checkLogin():
		user = u.get()
		pswd = encryptpsw(p.get())

		with open(f'files/login.txt', 'r') as f:
			logins =  f.readlines()
		for i in logins:
			i = i.split(',')
			if pswd == i[0].strip('\n') and user == i[1].strip('\n'):
				main(user.strip('\n'))
			else:
				continue

	def register():
		def addToFile():
			username = u.get()
			password = p.get()
			with open('files/login.txt', 'a') as f:
				f.write(f"{encryptpsw(password)},{username}\n")
			os.mkdir(f"files/{username}")
			files = ["card.txt", "notes.txt", "password.txt", "vault.txt"]
			for file in files:
				open(f"files/{username}/{file}", 'w').close()
			make_key(username)

		reg = Toplevel(root)
		reg.geometry("500x250")
		reg.resizable(False, False)
		Label(reg, text="Register", font=('arial', 20)).place(x=150,y=10)
		Label(reg, text="Username", font=('arial',20)).place(x=20,y=70)
		Label(reg, text="Password", font=('arial',20)).place(x=20,y=110)

		u = Entry(reg, font=('arial', 16))
		u.place(x=170, y=75, height=30, width=150)
		p = Entry(reg, font=('arial', 16))
		p.place(x=170, y=115, height=30, width=150)

		Button(reg, text="Register", font=('arial', 20), command=addToFile).place(x=110, y=160, height=35, width=150)

	dateTime = Label(root, text="", font=('arial', 15))
	dateTime.place(x=420, y=5)
	dateDay = Label(root, text="", font=('arial', 15))
	dateDay.place(x=10, y=5)
	get_time()

	Label(root, text="Welcome Back", font=('arial', 20)).place(x=160, y=10)
	Label(root, text="Please Login", font=('arial', 20)).place(x=175, y=40)
	u = Entry(root, font=('arial', 18), justify="center")
	u.place(x=150, y=85, height=30, width=200)
	p = Entry(root, font=('arial', 18), show="●", justify="center")
	p.place(x=150, y=120, height=30, width=200)
	Button(root, text="Login", font=('arial', 18), command=checkLogin).place(x=150, y=165, height=30, width=200)
	Button(root, text="Register", font=('arial', 18), command=register).place(x=150, y=200, height=30, width=200)

login()

root.mainloop()