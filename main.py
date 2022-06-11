from tkinter import *
from cryption import *
import time

root = Tk()
root.title("Password Manager")
root.geometry("400x300")
root.resizable(False, False)

# root.deiconify() re-open a window

def main(user):
	root.geometry("500x250")
	for widget in root.winfo_children():
		widget.destroy()
		
	def passwords():
		def displayPassword():
			for widget in main.winfo_children():
				if isinstance(widget, Entry):
					widget.destroy()
			f = open('files/password.txt', 'r')
			posY = 100
			posY1 = 100
			count = 1
			for line in f:
				entitySplit = line.split(",")
				site, user, pwd = decryptPWD(entitySplit[0], entitySplit[1], entitySplit[2])
				sVar, uVar, pVar, cVar = StringVar(), StringVar(), StringVar(), StringVar()
				
				cVar.set(count)
				sVar.set(site)
				uVar.set(user)
				pVar.set(pwd)
				if count <= 15:	
					Entry(main, textvariable=cVar, font=('arial', 15, 'bold')).place(x=0,y=posY, height=30, width=30)
					Entry(main, textvariable=sVar, font=('arial', 15)).place(x=30,y=posY, height=30, width=103)
					Entry(main, textvariable=uVar, font=('arial', 12)).place(x=133, y=posY, height=30, width=240)
					Entry(main, textvariable=pVar, font=('arial', 12)).place(x=373, y=posY, height=30, width=117)
					a.place(x=390, y=10)
					main.geometry(f"480x{posY+50}")
				else:
					Entry(main, textvariable=cVar, font=('arial', 15, 'bold')).place(x=490,y=posY1, height=30, width=30)
					Entry(main, textvariable=sVar, font=('arial', 15)).place(x=520,y=posY1, height=30, width=103)
					Entry(main, textvariable=uVar, font=('arial', 12)).place(x=623, y=posY1, height=30, width=240)
					Entry(main, textvariable=pVar, font=('arial', 12)).place(x=863, y=posY1, height=30, width=117)
					a.place(x=880, y=10)
					main.geometry(f"970x{posY+50}")
					posY1 += 30
				posY += 30
				count += 1
			

		def add():
			def addToFile():
				site, user, pswd = encryptPWD(s.get(), u.get(), p.get())
				with open('files/password.txt', 'a') as f:
					f.write(f"{site},{user},{pswd}\n")
				Label(add, text="Successfully added", font=('arial', 20)).place(x=20, y=250)
				displayPassword()
			add = Toplevel(main)
			add.title("Add Password")
			add.geometry("400x300")
			add.resizable(False, False)
			
			Label(add, text="Add Password", font=('arial', 20)).place(x=120, y=10)

			Label(add, text="Website", font=('arial', 20)).place(x=20, y=80)
			Label(add, text="Username", font=('arial', 20)).place(x=20, y=120)
			Label(add, text="Password", font=('arial', 20)).place(x=20, y=160)

			s = Entry(add, font=('arial', 15))
			s.place(x=160, y=85, height=30, width=180)
			u = Entry(add, font=('arial', 15))
			u.place(x=160, y=125, height=30, width=180)
			p = Entry(add, font=('arial', 15))
			p.place(x=160, y=165, height=30, width=180)

			Button(add, text="Add", font=('arial', 18), command=addToFile).place(x=30, y=200, height=30, width=290)

		def delete():
			def deleteFromFile():
				with open('files/password.txt', 'r') as f:
					lines = f.readlines()
				i = int(num.get())
				delLine = lines[i-1]
				with open('files/password.txt', 'w') as f:
					for line in lines:
						if line.strip("\n") != delLine.strip("\n"):	
							f.write(line) 
				displayPassword()
			dele = Toplevel(main)
			dele.title("Delete")
			dele.geometry("300x200")
			dele.resizable(False, False)
			
			Label(dele, text="Delete", font=('arial', 20)).place(x=110, y=10)
			Label(dele, text="Line Number", font=('arial', 20)).place(x=10, y=70)

			num = Entry(dele, font=('arial', 20))
			num.place(x=180, y=75, height=30, width=65)
			Button(dele, text="Delete", font=('airal', 20), command=deleteFromFile).place(x=20, y=110, height=30, width=210)
		def edit():
			def load():
				with open("files/password.txt", 'r') as f:
					lines = f.readlines()
				i = int(num.get())
				line = lines[i-1]
				line = line.split(',')
				ENsite, ENuser, ENpswd = line[0], line[1], line[2]
				DEsite, DEuser, DEpswd = decryptPWD(line[0], line[1], line[2])
				sVar.set(DEsite)
				uVar.set(DEuser)
				pVar.set(DEpswd)

			def save():
					newSite, newUser, newPswd = encryptPWD(s.get(), u.get(), p.get())
					with open("files/password.txt", 'r') as f:
						lines = f.readlines()
					i = int(num.get())
					with open("files/password.txt", 'w') as f:
							for line in lines:
								if line == lines[i-1]:
									print("Hello")
									f.write(f"{newSite},{newUser},{newPswd}\n")
								else:
									print("Goodbye")
									f.write(line)
					displayPassword()
			edit = Toplevel(main)
			edit.title("Edit")
			edit.geometry("500x350")
			edit.resizable(False, False)

			Label(edit, text="Edit", font=('arial', 20)).place(x=230, y=10)

			Label(edit, text="Line Number", font=('arial', 20)).place(x=20, y=70)
			num = Entry(edit, font=('arial', 20))
			num.place(x=180, y=75, height=30, width=65)

			Label(edit, text="Website", font=('arial', 20)).place(x=20, y=110)
			Label(edit, text="Username", font=('arial', 20)).place(x=20, y=150)
			Label(edit, text="Password", font=('arial', 20)).place(x=20, y=190)

			sVar, uVar, pVar = StringVar(), StringVar(), StringVar()
			s = Entry(edit, textvariable=sVar, font=('arial', 14))
			s.place(x=160, y=115, height=30, width=320)
			u = Entry(edit, textvariable=uVar, font=('arial', 14))
			u.place(x=160, y=155, height=30, width=320)
			p = Entry(edit, textvariable=pVar, font=('arial', 14))
			p.place(x=160, y=195, height=30, width=320)

			Button(edit, text="Save", font=('arial', 20), command=save).place(x=20, y=250, height=30, width=150)
			Button(edit, text="Load", font=('arial', 20), command=load).place(x=180, y=250, height=30, width=150)
		main = Toplevel(root)
		main.title("Passwords")
		main.geometry("480x450")
		main.resizable(False, False)

		Button(main, text="Add", font=('arial', 15), command=add).place(x=10, y=10, height=40, width=80)
		Button(main, text="Delete", font=('arial', 15), command=delete).place(x=10, y=55, height=40, width=80)
		Button(main, text="Edit", font=('arial', 15), command=edit).place(x=95, y=10, height=40, width=80)
		a=Button(main, text="Reload", font=('arial', 15), command=displayPassword)
		a.place(x=390, y=10, height=40, width=80)
		displayPassword()

	def cards():
		def displayCard():
			for widget in main.winfo_children():
				if isinstance(widget, Entry):
					widget.destroy()
			f = open('files/card.txt', 'r')
			posY = 100
			count = 1
			for line in f:
				entitySplit = line.split(",")
				name, num, date, ccv = decryptCRD(entitySplit[0], entitySplit[1], entitySplit[2], entitySplit[3])
				nVar, nuVar, dVar, cVar, coVar = StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
				
				coVar.set(count)
				nVar.set(name)
				nuVar.set(num)
				dVar.set(date)
				cVar.set(ccv)
				
				Entry(main, textvariable=coVar, font=('arial', 15, 'bold')).place(x=0,y=posY, height=30, width=30)
				Entry(main, textvariable=nVar, font=('arial', 15)).place(x=30,y=posY, height=30, width=103)
				Entry(main, textvariable=nuVar, font=('arial', 12)).place(x=133, y=posY, height=30, width=190)
				Entry(main, textvariable=dVar, font=('arial', 12)).place(x=323, y=posY, height=30, width=90)
				Entry(main, textvariable=cVar, font=('arial', 12)).place(x=413, y=posY, height=30, width=87)
				posY += 30
				count += 1
			main.geometry(f"500x{posY+50}")
		
		def add():
			def addToFile():
				name, num, date, ccv = encryptCRD(n.get(), nu.get(), d.get(), c.get())
				with open('files/card.txt', 'a') as f:
					f.write(f"{name},{num},{date},{ccv}\n")
				Label(add, text="Successfully added", font=('arial', 20)).place(x=20, y=40)
				displayCard()
			add = Toplevel(main)
			add.title("Add Card")
			add.geometry("400x300")
			add.resizable(False, False)
			
			Label(add, text="Add Card", font=('arial', 20)).place(x=120, y=10)

			Label(add, text="Name", font=('arial', 20)).place(x=20, y=80)
			Label(add, text="Numbers", font=('arial', 20)).place(x=20, y=120)
			Label(add, text="Date mm/yy", font=('arial', 20)).place(x=20, y=160)
			Label(add, text="CCV", font=('arial', 20)).place(x=20, y=200)

			n = Entry(add, font=('arial', 15))
			n.place(x=180, y=85, height=30, width=180)
			nu = Entry(add, font=('arial', 15))
			nu.place(x=180, y=125, height=30, width=180)
			d = Entry(add, font=('arial', 15))
			d.place(x=180, y=165, height=30, width=180)
			c = Entry(add, font=('arial', 15))
			c.place(x=180, y=205, height=30, width=180)

			Button(add, text="Add", font=('arial', 18), command=addToFile).place(x=30, y=260, height=30, width=290)

		def delete():
			def deleteFromFile():
				with open('files/card.txt', 'r') as f:
					lines = f.readlines()
				i = int(num.get())
				delLine = lines[i-1]
				with open('files/card.txt', 'w') as f:
					for line in lines:
						if line.strip("\n") != delLine.strip("\n"):	
							f.write(line) 
				displayCard()
			dele = Toplevel(main)
			dele.title("Delete")
			dele.geometry("300x200")
			dele.resizable(False, False)
			
			Label(dele, text="Delete", font=('arial', 20)).place(x=110, y=10)
			Label(dele, text="Line Number", font=('arial', 20)).place(x=10, y=70)

			num = Entry(dele, font=('arial', 20))
			num.place(x=180, y=75, height=30, width=65)
			Button(dele, text="Delete", font=('airal', 20), command=deleteFromFile).place(x=20, y=110, height=30, width=210)

		def edit():
			def load():
				with open("files/card.txt", 'r') as f:
					lines = f.readlines()
				i = int(num.get())
				line = lines[i-1]
				line = line.split(',')
				ENname, ENnum, ENdate, ENccv = line[0], line[1], line[2], line[3]
				DEname, DEnum, DEdate, DEccv = decryptCRD(line[0], line[1], line[2], line[3])
				nVar.set(DEname)
				nuVar.set(DEnum)
				dVar.set(DEdate)
				cVar.set(DEccv)

			def save():
					newName, newNum, newDate, newCcv = encryptCRD(n.get(), nu.get(), d.get(), c.get())
					with open("files/card.txt", 'r') as f:
						lines = f.readlines()
					i = int(num.get())
					with open("files/card.txt", 'w') as f:
							for line in lines:
								if line == lines[i-1]:
									print("Hello")
									f.write(f"{newName},{newNum},{newDate},{newCcv}\n")
								else:
									print("Goodbye")
									f.write(line)
					displayCard()
			edit = Toplevel(main)
			edit.title("Edit")
			edit.geometry("500x350")
			edit.resizable(False, False)

			Label(edit, text="Edit", font=('arial', 20)).place(x=230, y=10)

			Label(edit, text="Line Number", font=('arial', 20)).place(x=20, y=70)
			num = Entry(edit, font=('arial', 20))
			num.place(x=180, y=75, height=30, width=65)

			Label(edit, text="Name", font=('arial', 20)).place(x=20, y=110)
			Label(edit, text="Number", font=('arial', 20)).place(x=20, y=150)
			Label(edit, text="Date", font=('arial', 20)).place(x=20, y=190)
			Label(edit, text="Ccv", font=('arial', 20)).place(x=20, y=230)

			nVar, nuVar, dVar, cVar = StringVar(), StringVar(), StringVar(), StringVar()
			n = Entry(edit, textvariable=nVar, font=('arial', 14))
			n.place(x=160, y=115, height=30, width=320)
			nu = Entry(edit, textvariable=nuVar, font=('arial', 14))
			nu.place(x=160, y=155, height=30, width=320)
			d = Entry(edit, textvariable=dVar, font=('arial', 14))
			d.place(x=160, y=195, height=30, width=320)
			c = Entry(edit, textvariable=cVar, font=('arial', 14))
			c.place(x=160, y=235, height=30, width=320)

			Button(edit, text="Save", font=('arial', 20), command=save).place(x=20, y=290, height=30, width=150)
			Button(edit, text="Load", font=('arial', 20), command=load).place(x=180, y=290, height=30, width=150)

		main = Toplevel(root)
		main.title("Passwords")
		main.geometry("480x450")
		main.resizable(False, False)

		Button(main, text="Add", font=('arial', 15), command=add).place(x=10, y=10, height=40, width=80)
		Button(main, text="Delete", font=('arial', 15), command=delete).place(x=10, y=55, height=40, width=80)
		Button(main, text="Edit", font=('arial', 15), command=edit).place(x=95, y=10, height=40, width=80)
		Button(main, text="Reload", font=('arial', 15), command=displayCard).place(x=390, y=10, height=40, width=80)
		displayCard()

	def changePass():
		def save():
			with open('files/login.txt', 'r') as f:
				a = f.read().split(',')
			usernameNEW = u.get()
			passwordNEW = p.get()
			usernameOLD = a[1]
			passwordOLD = a[0]
			with open('files/login.txt', 'w') as f: 
				if usernameNEW == "":
					f.write(f"{encryptpsw(passwordNEW)},{usernameOLD}")
				elif passwordNEW == "":
					f.write(f"{passwordOLD},{usernameNEW}")
				else:
					f.write(f"{encryptpsw(passwordNEW)},{usernameNEW}")
			
		change = Toplevel(root)
		change.title("Change Password")
		change.geometry("400x300")
		
		Label(change, text="Change Password/Username", font=('arial', 20)).place(x=20,y=10)

		Label(change, text="Username", font=('arial',20)).place(x=20,y=70)
		Label(change, text="Password", font=('arial',20)).place(x=20,y=110)
		u = Entry(change, font=('arial', 16))
		u.place(x=170, y=75, height=30, width=150)
		p = Entry(change, font=('arial', 16))
		p.place(x=170, y=115, height=30, width=150)
		Button(change, text="Save", font=('arial', 20), command=save).place(x=20, y=170, height=35, width=150)	

	Label(root, text=f"Hello {user}!", font=('arial', 25)).place(x=165, y=10)
	
	Button(root, text="Passwords", font=('arial', 20), command=passwords).place(x=35, y=75, height=40, width=150)
	Button(root, text="Cards", font=('arial', 20), command=cards).place(x=35, y=130, height=40, width=150)
	Button(root, text="Change Password", font=('arial', 12), command=changePass).place(x=35, y=185, height=40, width=150)

def login():
	passwd = passwordEntry.get()
	passwd = encryptpsw(passwd)
	with open('files/login.txt', 'r') as f:
		pwd = f.read().split(',')
	if passwd == pwd[0].strip('\n'):
		main(pwd[1].strip('\n'))
	else:
		Label(root, text="Wrong Password", font=('arial', 20)).place(x=20, y=210)

Label(root, text="Welcome Back", font=('arial', 20)).place(x=110, y=10)
Label(root, text="Please Login", font=('arial', 20)).place(x=125, y=40)

Label(root, text="Password", font=('arial', 18)).place(x=20, y=130)
passwordEntry = Entry(root, font=('arial', 15))
passwordEntry.place(x=140, y=135, height=25, width=130)
Button(root, text="Login", font=('arial', 18), command=login).place(x=20, y=170, height=30, width=250)

root.mainloop()
