from tkinter import *
from cryption import *
import random
import string
import shutil
import os

show = True

def passwords(root, user):
	def showPassword(user):
		global show
		show = not show
		if show:
			b.config(text="Show")
		else:
			b.config(text="Hide")
		updateP(show, user)
	def updateP(show, name):
		for widget in main.winfo_children():
			if isinstance(widget, Entry):
				widget.destroy()
		f = open(f'files/{name}/password.txt', 'r')
		posY = 100
		posY1 = 100
		count = 1
		for line in f:
			entitySplit = line.split(",")
			site, user, pwd = decryptPWD(name, entitySplit[0], entitySplit[1], entitySplit[2])
			sVar, uVar, pVar, cVar = StringVar(), StringVar(), StringVar(), StringVar()
			
			cVar.set(count)
			sVar.set(site)
			uVar.set(user)
			pVar.set(pwd)
			if show == True:
				if count <= 15:	
					Entry(main, textvariable=cVar, font=('arial', 15, 'bold'), justify="center").place(x=0,y=posY, height=30, width=30)
					Entry(main, textvariable=sVar, font=('arial', 15)).place(x=30,y=posY, height=30, width=103)
					Entry(main, textvariable=uVar, font=('arial', 12)).place(x=133, y=posY, height=30, width=250)
					Entry(main, textvariable=pVar, font=('arial', 12), show="*").place(x=383, y=posY, height=30, width=117)
					a.place(x=410, y=10)
					b.place(x=410, y=55)
					main.geometry(f"500x{posY+30}")
				else:
					Entry(main, textvariable=cVar, font=('arial', 15, 'bold'), justify="center").place(x=490,y=posY1, height=30, width=30)
					Entry(main, textvariable=sVar, font=('arial', 15)).place(x=520,y=posY1, height=30, width=103)
					Entry(main, textvariable=uVar, font=('arial', 12)).place(x=623, y=posY1, height=30, width=240)
					Entry(main, textvariable=pVar, font=('arial', 12), show="*").place(x=863, y=posY1, height=30, width=117)
					a.place(x=880, y=10)
					b.place(x=880, y=55)
					main.geometry(f"970x{posY+30}")
					posY1 += 30
			elif show == False:
				if count <= 15:	
					Entry(main, textvariable=cVar, font=('arial', 15, 'bold'), justify="center").place(x=0,y=posY, height=30, width=30)
					Entry(main, textvariable=sVar, font=('arial', 15)).place(x=30,y=posY, height=30, width=103)
					Entry(main, textvariable=uVar, font=('arial', 12)).place(x=133, y=posY, height=30, width=250)
					Entry(main, textvariable=pVar, font=('arial', 12)).place(x=383, y=posY, height=30, width=117)
					a.place(x=410, y=10)
					b.place(x=410, y=55)
					main.geometry(f"500x{posY+30}")
				else:
					Entry(main, textvariable=cVar, font=('arial', 15, 'bold'), justify="center").place(x=490,y=posY1, height=30, width=30)
					Entry(main, textvariable=sVar, font=('arial', 15)).place(x=520,y=posY1, height=30, width=103)
					Entry(main, textvariable=uVar, font=('arial', 12)).place(x=623, y=posY1, height=30, width=240)
					Entry(main, textvariable=pVar, font=('arial', 12)).place(x=863, y=posY1, height=30, width=117)
					a.place(x=880, y=10)
					b.place(x=880, y=55)
					main.geometry(f"970x{posY+30}")
					posY1 += 30
			posY += 30
			count += 1
		main.title(f"Passwords | Total: {count-1}")
		main.geometry(f"500x{posY}")
	def add(user):
		def genPass():
			chars = string.ascii_letters + string.digits
			pVar = StringVar()
			pVar.set("".join(random.sample(chars, 10)))
			p.config(textvariable=pVar)
		def addToFile(name):
			site, user, pswd = encryptPWD(name, s.get(), u.get(), p.get())
			with open(f'files/{name}/password.txt', 'a') as f:
				f.write(f"{site},{user},{pswd}\n")
			Label(add, text="Successfully added", font=('arial', 20)).place(x=20, y=250)
			updateP(show, name)
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

		Button(add, text="Add", font=('arial', 18), command=lambda:addToFile(user)).place(x=25, y=200, height=35, width=150)
		Button(add, text="Generate Password", font=('arial', 13), command=genPass).place(x=185, y=200, height=35, width=150)
	def delete(user):
		def deleteFromFile(user):
			with open(f'files/{user}/password.txt', 'r') as f:
				lines = f.readlines()
			i = int(num.get())
			delLine = lines[i-1]
			with open(f'files/{user}/password.txt', 'w') as f:
				for line in lines:
					if line.strip("\n") != delLine.strip("\n"):	
						f.write(line) 
			updateP(show, user)
		dele = Toplevel(main)
		dele.title("Delete")
		dele.geometry("300x200")
		dele.resizable(False, False)
		
		Label(dele, text="Delete", font=('arial', 20)).place(x=110, y=10)
		Label(dele, text="Line Number", font=('arial', 20)).place(x=10, y=70)

		num = Entry(dele, font=('arial', 20))
		num.place(x=180, y=75, height=30, width=65)
		Button(dele, text="Delete", font=('airal', 20), command=lambda:deleteFromFile(user)).place(x=20, y=110, height=30, width=210)
	def edit(user):
		def load(user):
			with open(f"files/{user}/password.txt", 'r') as f:
				lines = f.readlines()
			i = int(num.get())
			line = lines[i-1]
			line = line.split(',')
			ENsite, ENuser, ENpswd = line[0], line[1], line[2]
			DEsite, DEuser, DEpswd = decryptPWD(user, line[0], line[1], line[2])

			sVar.set(DEsite)
			uVar.set(DEuser)
			pVar.set(DEpswd)

		def save(user):
				newSite, newUser, newPswd = encryptPWD(user, s.get(), u.get(), p.get())
				with open(f"files/{user}/password.txt", 'r') as f:
					lines = f.readlines()
				i = int(num.get())
				with open(f"files/{user}/password.txt", 'w') as f:
						for line in lines:
							if line == lines[i-1]:
								f.write(f"{newSite},{newUser},{newPswd}\n")
							else:
								f.write(line)
				updateP(show, user)
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

		Button(edit, text="Save", font=('arial', 20), command=lambda:save(user)).place(x=20, y=290, height=30, width=150)
		Button(edit, text="Load", font=('arial', 20), command=lambda:load(user)).place(x=180, y=290, height=30, width=150)

	main = Toplevel(root)
	main.title("Passwords")
	main.geometry("500x450")
	main.resizable(False, False)
	Button(main, text="Add", font=('arial', 15), command=lambda:add(user)).place(x=10, y=10, height=40, width=80)
	Button(main, text="Delete", font=('arial', 15), command=lambda:delete(user)).place(x=10, y=55, height=40, width=80)
	Button(main, text="Edit", font=('arial', 15), command=lambda:edit(user)).place(x=95, y=10, height=40, width=80)
	a=Button(main, text="Reload", font=('arial', 15), command=lambda:updateP(show, user))
	a.place(x=410, y=10, height=40, width=80)
	b = Button(main, text="Show", font=('arial', 15), command=lambda:showPassword(user))
	b.place(x=410, y=55, height=40, width=80)
	updateP(show, user)

def cards(root, user):
	def updateC(user):
		for widget in main.winfo_children():
			if isinstance(widget, Entry):
				widget.destroy()
		f = open(f'files/{user}/card.txt', 'r')
		posY = 100
		count = 1
		for line in f:
			entitySplit = line.split(",")
			name, num, date, ccv = decryptCRD(user, entitySplit[0], entitySplit[1], entitySplit[2], entitySplit[3])
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
		main.geometry(f"500x{posY}")
		main.title(f"Cards | Total: {count-1}")
	def add(user):
		def addToFile(user):
			name, num, date, ccv = encryptCRD(user, n.get(), nu.get(), d.get(), c.get())
			with open(f'files/{user}/card.txt', 'a') as f:
				f.write(f"{name},{num},{date},{ccv}\n")
			Label(add, text="Successfully added", font=('arial', 20)).place(x=20, y=40)
			updateC(user)
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

		Button(add, text="Add", font=('arial', 18), command=lambda:addToFile(user)).place(x=30, y=260, height=30, width=290)
	def delete(user):
		def deleteFromFile(user):
			with open(f'files/{user}/card.txt', 'r') as f:
				lines = f.readlines()
			i = int(num.get())
			delLine = lines[i-1]
			with open(f'files/{user}/card.txt', 'w') as f:
				for line in lines:
					if line.strip("\n") != delLine.strip("\n"):	
						f.write(line) 
			updateC(user)
		dele = Toplevel(main)
		dele.title("Delete")
		dele.geometry("300x200")
		dele.resizable(False, False)
		
		Label(dele, text="Delete", font=('arial', 20)).place(x=110, y=10)
		Label(dele, text="Line Number", font=('arial', 20)).place(x=10, y=70)

		num = Entry(dele, font=('arial', 20))
		num.place(x=180, y=75, height=30, width=65)
		Button(dele, text="Delete", font=('airal', 20), command=lambda:deleteFromFile(user)).place(x=20, y=110, height=30, width=210)
	def edit(user):
		def load(user):
			with open(f"files/{user}/card.txt", 'r') as f:
				lines = f.readlines()
			i = int(num.get())
			line = lines[i-1]
			line = line.split(',')
			ENname, ENnum, ENdate, ENccv = line[0], line[1], line[2], line[3]
			DEname, DEnum, DEdate, DEccv = decryptCRD(user, line[0], line[1], line[2], line[3])
			nVar.set(DEname)
			nuVar.set(DEnum)
			dVar.set(DEdate)
			cVar.set(DEccv)

		def save(user):
				newName, newNum, newDate, newCcv = encryptCRD(user, n.get(), nu.get(), d.get(), c.get())
				with open(f"files/{user}/card.txt", 'r') as f:
					lines = f.readlines()
				i = int(num.get())
				with open(f"files/{user}/card.txt", 'w') as f:
						for line in lines:
							if line == lines[i-1]:
								f.write(f"{newName},{newNum},{newDate},{newCcv}\n")
							else:
								f.write(line)
				updateC(user)
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

		Button(edit, text="Save", font=('arial', 20), command=lambda:save(user)).place(x=20, y=290, height=30, width=150)
		Button(edit, text="Load", font=('arial', 20), command=lambda:load(user)).place(x=180, y=290, height=30, width=150)

	main = Toplevel(root)
	main.title("Passwords")
	main.geometry("480x450")
	main.resizable(False, False)

	Button(main, text="Add", font=('arial', 15), command=lambda:add(user)).place(x=10, y=10, height=40, width=80)
	Button(main, text="Delete", font=('arial', 15), command=lambda:delete(user)).place(x=10, y=55, height=40, width=80)
	Button(main, text="Edit", font=('arial', 15), command=lambda:edit(user)).place(x=95, y=10, height=40, width=80)
	Button(main, text="Reload", font=('arial', 15), command=lambda:updateC(user)).place(x=410, y=10, height=40, width=80)
	updateC(user)

def vault(root, user):
		def updateV(user):
			for widget in main.winfo_children():
				if isinstance(widget, Entry):
					widget.destroy()
			f = open(f'files/{user}/vault.txt', 'r')
			posY = 100
			count = 1
			for line in f:
				addrPriv = line.split(',')
				deADDR, dePRIV, deNAME = decryptCRO(user, addrPriv[0], addrPriv[1], addrPriv[2])
				addr, priv, name, c = StringVar(), StringVar(), StringVar(), StringVar()
				addr.set(deADDR)
				priv.set(dePRIV)
				name.set(deNAME)
				c.set(count)
				Entry(main, textvariable=c, font=('arial', 15, 'bold')).place(x=0, y=posY, width=30, height=30)
				Entry(main, textvariable=addr, font=('arial', 9)).place(x=30,y=posY, width=330, height=30)
				Entry(main, textvariable=priv, font=('arial', 8)).place(x=360, y=posY, width=640, height=30)
				Entry(main, textvariable=name, font=('arial', 15)).place(x=1000, y=posY, width=100, height=30)
				posY += 30
				count += 1
			main.geometry(f"1100x{posY}")
			main.title(f"Vault | Total: {count-1}")
		def add(user):
			add = Toplevel(main)
			add.title("Add")
			add.geometry("500x300")
			add.resizable(False, False)
			def addToFile(user):
				addr, priv, name = addrEntry.get(), privEntry.get(), nameEntry.get() 
				enADDR, enPRIV, enNAME = encryptCRO(user, addr, priv, name)
				with open(f"files/{user}/vault.txt", 'a') as f:
					f.write(f"{enADDR},{enPRIV},{enNAME}\n")
				updateV(user)
				
			addrEntry = Entry(add, font=('arial', 14))
			addrEntry.place(x=150, y=60, height=30, width=200)
			Label(add, text="Adress", font=('arial',20)).place(x=25, y=50)
			
			privEntry = Entry(add, font=('arial', 14))
			privEntry.place(x=150, y=110, height=30, width=200)
			Label(add, text="Key", font=('arial',20)).place(x=25, y=100)
			
			nameEntry = Entry(add, font=('arial', 14))
			nameEntry.place(x=150, y=160, height=30, width=200)
			Label(add, text="Name", font=('arial',20)).place(x=25, y=150)

			Label(add, text="Add", font=('arial', 20)).place(x=230, y=10)
			Button(add, text="Add", font=('arial', 20), command=lambda:addToFile(user)).place(x=220, y=230)
		def delete(user):
			def deleteFromFile(user):
				with open(f'files/{user}/vault.txt', 'r') as f:
					lines = f.readlines()
				i = int(num.get())
				delLine = lines[i-1]
				with open(f'files/{user}/vault.txt', 'w') as f:
					for line in lines:
						if line.strip("\n") != delLine.strip("\n"):	
							f.write(line) 
				updateV(user)
			dele = Toplevel(main)
			dele.title("Delete")
			dele.geometry("300x200")
			dele.resizable(False, False)
			
			Label(dele, text="Delete", font=('arial', 20)).place(x=110, y=10)
			Label(dele, text="Line Number", font=('arial', 20)).place(x=10, y=70)

			num = Entry(dele, font=('arial', 20))
			num.place(x=180, y=75, height=30, width=65)
			Button(dele, text="Delete", font=('airal', 20), command=lambda:deleteFromFile(user)).place(x=20, y=110, height=30, width=210)
		def edit(user):
			def load(user):
				with open(f"files/{user}/vault.txt", 'r') as f:
					lines = f.readlines()
				i = int(num.get())
				line = lines[i-1]
				line = line.split(',')
				ENaddr, ENpriv, ENname = line[0], line[1], line[2]
				DEaddr, DEpriv, DEname = decryptCRO(user, line[0], line[1], line[2])
				aVar.set(DEaddr)
				pVar.set(DEpriv)
				nVar.set(DEname)

			def save(user):
					newAddr, newPriv, newName = encryptCRO(user, a.get(), p.get(), n.get())
					with open(f"files/{user}/vault.txt", 'r') as f:
						lines = f.readlines()
					i = int(num.get())
					with open(f"files/{user}/vault.txt", 'w') as f:
							for line in lines:
								if line == lines[i-1]:
									f.write(f"{newAddr},{newPriv},{newName}\n")
								else:
									f.write(line)
					updateV(user)
			edit = Toplevel(main)
			edit.title("Edit")
			edit.geometry("500x350")
			edit.resizable(False, False)

			Label(edit, text="Edit", font=('arial', 20)).place(x=230, y=10)

			Label(edit, text="Line Number", font=('arial', 20)).place(x=20, y=70)
			num = Entry(edit, font=('arial', 20))
			num.place(x=180, y=75, height=30, width=65)

			Label(edit, text="Addres", font=('arial', 20)).place(x=20, y=110)
			Label(edit, text="Key", font=('arial', 20)).place(x=20, y=150)
			Label(edit, text="Name", font=('arial', 20)).place(x=20, y=190)

			aVar, pVar, nVar = StringVar(), StringVar(), StringVar()
			a = Entry(edit, textvariable=aVar, font=('arial', 14))
			a.place(x=160, y=115, height=30, width=320)
			p = Entry(edit, textvariable=pVar, font=('arial', 14))
			p.place(x=160, y=155, height=30, width=320)
			n = Entry(edit, textvariable=nVar, font=('arial', 14))
			n.place(x=160, y=195, height=30, width=320)
			Button(edit, text="Save", font=('arial', 20), command=lambda:save(user)).place(x=20, y=290, height=30, width=150)
			Button(edit, text="Load", font=('arial', 20), command=lambda:load(user)).place(x=180, y=290, height=30, width=150)

		main = Toplevel(root)
		main.title("Vault")
		main.geometry("1100x300")
		main.resizable(False, False)
		Button(main, text="Add", font=('arial', 15), command=lambda:add(user)).place(x=10, y=10, height=40, width=80)
		Button(main, text="Delete", font=('arial', 15), command=lambda:delete(user)).place(x=10, y=55, height=40, width=80)
		Button(main, text="Edit", font=('arial', 15), command=lambda:edit(user)).place(x=95, y=10, height=40, width=80)
		Button(main, text="Reload", font=('arial', 15), command=lambda:updateV(user)).place(x=1000, y=10, height=40, width=80)
		updateV(user)

def notes(root, user):
		def load(user):
			with open(f"files/{user}/notes.txt" , 'r') as f:
				lines = f.readlines()
				for line in lines:
					a.insert(END, line)
		def save(user):
			contents = a.get(1.0, END)
			with open(f"files/{user}/notes.txt", 'w') as f:
				f.write(contents)
		def clear():
			contents = a.get(1.0, END)
			for i in contents:
				a.replace(1.0, END, i, "")

		main = Toplevel(root)
		main.title("Notes")
		main.geometry("550x500")
		main.resizable(False, False)

		Button(main, text="Save",  font=('arial', 20), command=lambda:save(user) ).place(x=10, y=10, height=30, width=140)
		Button(main, text="Clear", font=('arial', 20), command=clear).place(x=400, y=10, height=30, width=140)
		a = Text(main, font=('arial', 14))
		a.place(x=0, y=80, height=420, width=550)
		load(user)

def changePass(root, user):
	def save():
		with open('files/login.txt', 'r') as f:
			lines = f.readlines()
		uOLD, pOLD, uNEW, pNEW = user, encryptpsw(pp.get()), u.get(), encryptpsw(p.get())
		with open('files/login.txt', 'w') as f: 
			for line in lines:
				if line.strip("\n") == f"{pOLD},{uOLD}":
					if uNEW == "":
						f.write(f"{pNEW},{uOLD}\n")
					elif pNEW == "":
						f.write(f"{pOLD},{uNEW}\n")
						os.rename(f"files/{uOLD}", f"files/{uNEW}")
					else:
						f.write(f"{pNEW},{uNEW}\n")
						os.rename(f"files/{uOLD}", f"files/{uNEW}")
				else:
					f.write(line)
	
	change = Toplevel(root)
	change.title("Change Password")
	change.geometry("400x300")
	
	Label(change, text="Change Password/Username", font=('arial', 20)).place(x=20,y=10)

	Label(change, text="Username", font=('arial',20)).place(x=20,y=70)
	Label(change, text="Password", font=('arial',20)).place(x=20,y=110)
	Label(change, text="Old Password", font=('arial',16)).place(x=20,y=155)
	u = Entry(change, font=('arial', 16))
	u.place(x=170, y=75, height=30, width=150)
	p = Entry(change, font=('arial', 16))
	p.place(x=170, y=115, height=30, width=150)
	pp = Entry(change, font=('arial', 16))
	pp.place(x=170, y=155, height=30, width=150)
	Button(change, text="Save", font=('arial', 20), command=save).place(x=20, y=200, height=35, width=150)	

def delete(root, user):
	def deleteFromFile(user):
		if p.get() != "":
			with open(f'files/login.txt', 'r') as f:
				lines = f.readlines()
			delAcc = encryptpsw(p.get()) + "," + user
			with open(f'files/login.txt', 'w') as f:
				for line in lines:
					if delAcc != line.strip("\n"):	
						f.write(line)
			shutil.rmtree(f"files/{user}")
		else:
			pass
	main = Toplevel(root)
	main.title("Delete")
	main.geometry("400x250")
	main.resizable(False, False)

	Label(main, text="Are you sure?", font=('arial', 20)).place(x=120, y=10)
	Label(main, text="Password", font=('arial', 20)).place(x=20, y=95)
	Label(main, text="Enter your password to confirm", font=('arial', 16)).place(x=25, y=130)

	p = Entry(main, font=('arial', 18))
	p.place(x=150, y=100, height=30, width=180)

	Button(main, text="Confirm", font=('arial', 20), command=lambda:deleteFromFile(user)).place(x=20, y=170, height=30, width=130)
