from tkinter import *
from cryption import *
from PIL import ImageTk, Image
import random
import string
import shutil
import qrcode
import json
import os

show = True

def password(display, controls, user):
    for widget in controls.winfo_children(): widget.destroy()
            
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
        add = Toplevel(display)
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
        dele = Toplevel(display)
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
        edit = Toplevel(display)
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
    def updateP(show, name):
        for widget in display.winfo_children():
            widget.destroy()
        
        f = open(f'files/{name}/password.txt', 'r')
        posY = 120
        count = 1
        for line in f:
            entitySplit = line.split(",")
            site, user, pwd = decryptPWD(name, entitySplit[0], entitySplit[1], entitySplit[2])
            sVar, uVar, pVar, cVar = StringVar(), StringVar(), StringVar(), StringVar()
			
            cVar.set(count)
            sVar.set(site)
            uVar.set(user)
            pVar.set(pwd)
            if show:
                Entry(display, textvariable=cVar, font=('arial', 20, 'bold'), justify="center").place(x=0,y=posY, height=50, width=40)
                Entry(display, textvariable=sVar, font=('arial', 20)).place(x=40,y=posY, height=50, width=163)
                Entry(display, textvariable=uVar, font=('arial', 20)).place(x=193, y=posY, height=50, width=550)
                Entry(display, textvariable=pVar, font=('arial', 20), show="●").place(x=740, y=posY, height=50, width=260)
            else:
                Entry(display, textvariable=cVar, font=('arial', 20, 'bold'), justify="center").place(x=0,y=posY, height=50, width=40)
                Entry(display, textvariable=sVar, font=('arial', 20)).place(x=40,y=posY, height=50, width=153)
                Entry(display, textvariable=uVar, font=('arial', 20)).place(x=193, y=posY, height=50, width=550)
                Entry(display, textvariable=pVar, font=('arial', 20)).place(x=740, y=posY, height=50, width=260)
            posY += 50
            count += 1
        Label(controls, text="Passwords", font=('arial', 40), bg="#4a4a4a").place(x=355, y=10)
        Label(controls, text=f"Count: {count-1}", font=('arial', 25), bg="#4a4a4a").place(x=400, y=65)
    def showPassword(user):
        global show
        show = not show
        if show:
            b.config(text="Show")
        else:
            b.config(text="Hide")
        updateP(show, user)

    Button(controls, text="Add", font=('arial', 25), command=lambda:add(user)).place(x=10, y=10, height=50, width=95)
    Button(controls, text="Delete", font=('arial', 25), command=lambda:delete(user)).place(x=10, y=70, height=50, width=95)
    Button(controls, text="Edit", font=('arial', 25), command=lambda:edit(user)).place(x=115, y=10, height=50, width=95)
    Button(controls, text="Reload", font=('arial', 21), command=lambda:updateP(show, user)).place(x=916, y=10, height=50, width=95)
    b = Button(controls, text="Show", font=('arial', 25), command=lambda:showPassword(user))
    b.place(x=916, y=70, height=50, width=95)
    updateP(show, user)

def card(display, controls, user):
    for widget in controls.winfo_children(): widget.destroy()
            
    def updateC(show, user):
        for widget in display.winfo_children(): widget.destroy()
            
        f = open(f'files/{user}/card.txt', 'r')
        posY = 120
        count = 1
        for line in f:
            entitySplit = line.split(",")
            name, num, date, ccv = decryptCRD(user, entitySplit[0], entitySplit[1], entitySplit[2], entitySplit[3])
            nVar, nuVar, dVar, cVar, coVar = StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
            
            coVar.set(count)
            nVar.set(name)
            dVar.set(date)
            cVar.set(ccv)
            if show == True:
                size = len(num)   
                if size == 19:
                    nuVar.set(num.replace(num[size - 9:], "●●●● ●●●●"))
                elif size == 16:
                    nuVar.set(num.replace(num[size - 8:], "●●●●●●●●"))
                Entry(display, textvariable=coVar, font=('arial', 20, 'bold'), justify="center").place(x=0,   y=posY, height=50, width=40)
                Entry(display, textvariable=nVar,  font=('arial', 22)).place(x=40,  y=posY, height=50, width=350)
                Entry(display, textvariable=nuVar, font=('arial', 22)).place(x=350, y=posY, height=50, width=350)
                Entry(display, textvariable=dVar,  font=('arial', 22), justify="center").place(x=700, y=posY, height=50, width=150)
                Entry(display, textvariable=cVar,  font=('arial', 22), show="●").place(x=850, y=posY, height=50, width=150)
            elif show == False:
                nuVar.set(num)
                Entry(display, textvariable=coVar, font=('arial', 20, 'bold'), justify="center").place(x=0,   y=posY, height=50, width=40)
                Entry(display, textvariable=nVar,  font=('arial', 22)).place(x=40,  y=posY, height=50, width=350)
                Entry(display, textvariable=nuVar, font=('arial', 22)).place(x=350, y=posY, height=50, width=350)
                Entry(display, textvariable=dVar,  font=('arial', 22), justify="center").place(x=700, y=posY, height=50, width=150)
                Entry(display, textvariable=cVar,  font=('arial', 22)).place(x=850, y=posY, height=50, width=150)
            posY += 50
            count += 1
        Label(controls, text="Cards", font=('arial', 40), bg="#4a4a4a").place(x=390, y=10)
        Label(controls, text=f"Count: {count-1}", font=('arial', 25), bg="#4a4a4a").place(x=400, y=65)
    def add(user):
        def addToFile(user):
            name, num, date, ccv = encryptCRD(user, n.get(), nu.get(), d.get(), c.get())
            with open(f'files/{user}/card.txt', 'a') as f:
                f.write(f"{name},{num},{date},{ccv}\n")
            Label(add, text="Successfully added", font=('arial', 20)).place(x=20, y=40)
            updateC(show, user)
        add = Toplevel(display)
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
            updateC(show, user)
        dele = Toplevel(display)
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
                updateC(show, user)
        edit = Toplevel(display)
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
    def showCard(user):
        global show
        show = not show
        if show:
            b.config(text="Show")
        else:
            b.config(text="Hide")
        updateC(show, user)

    Button(controls, text="Add", font=('arial', 25), command=lambda:add(user)).place(x=10, y=10, height=50, width=95)
    Button(controls, text="Delete", font=('arial', 25), command=lambda:delete(user)).place(x=10, y=70, height=50, width=95)
    Button(controls, text="Edit", font=('arial', 25), command=lambda:edit(user)).place(x=115, y=10, height=50, width=95)
    Button(controls, text="Reload", font=('arial', 21), command=lambda:updateC(show, user)).place(x=916, y=10, height=50, width=95)
    b = Button(controls, text="Show", font=('arial', 25), command=lambda:showCard(user))
    b.place(x=916, y=70, height=50, width=95)
    updateC(show, user)

def settings(display, controls, user): 
    for widget in display.winfo_children(): widget.destroy()
    for widget in controls.winfo_children(): widget.destroy()  
        
    def changePWD():
        for widget in display.winfo_children(): widget.destroy()
            
        def save(user):
            with open('files/login.txt', 'r') as f:
                lines = f.readlines()
            oldP, newP = encryptpsw(op.get()), encryptpsw(np.get())
            with open('files/login.txt', 'w') as f: 
                for line in lines:
                    if line.strip("\n") == f"{oldP},{user}":
                        f.write(f"{newP},{user}\n")
                        Label(display, text="Password was changed!", font=('arial', 30), bg="white").place(x=100, y=450)
                    else:
                        f.write(line)

        Label(display, text="Old Password", font=('arial', 30), bg="white").place(x=100, y=250)
        Label(display, text="New Password", font=('arial', 30), bg="white").place(x=100, y=320)

        op = Entry(display, font=('arial', 20))
        op.place(x=380, y=255, width=250, height=40)
        np = Entry(display, font=('arial', 20))
        np.place(x=380, y=325, width=250, height=40)

        Button(display, text="Save", font=('arial', 25), command=lambda:save(user)).place(x=120, y=380, width=250, height=50)
    def deleteACC():
        for widget in display.winfo_children(): widget.destroy()

        def delete(user):
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

        Label(display, text="Are you sure?", font=('arial', 35), bg="white").place(x=150, y=200)
        Label(display, text="Password", font=('arial', 27), bg="white").place(x=70, y=265)

        p = Entry(display, font=('arial', 20))
        p.place(x=250, y=270, width=250, height=40)

        Button(display, text="Delete", font=('arial', 25), command=lambda:delete(user)).place(x=150, y=320, height=50, width=250)
    def otp():
        for widget in display.winfo_children(): widget.destroy()
        with open(f'files/{user}/config/otp.json', 'r') as f: data = json.load(f)
        key = data["key"] 
        def active():
            with open(f'files/{user}/config/otp.json', 'r') as f:
                data = json.load(f)

            aOTP = data["active"]
            aOTP = not aOTP
            
            if aOTP:
                activeOTP.config(text="On")
                otpText.config(text="Two-Factor Authentication is Active")
            else:
                activeOTP.config(text="Off")
                otpText.config(text="Two-Factor Authentication is Disabled")

            with open(f'files/{user}/config/otp.json', 'w') as f:
                json.dump({"active":aOTP, "key":data['key']}, f)
            
        if data['active']: data = "On"; otpT = "Two-Factor Authentication is Active"
        else: data = "Off"; otpT = "Two-Factor Authentication is Disabled"

        
        uri = pyotp.totp.TOTP(key).provisioning_uri(name=user, issuer_name="")
        qrcode.make(uri).save(f'files/{user}/config/temp.png')
        img = ImageTk.PhotoImage(Image.open(f"files/{user}/config/temp.png").resize((350, 350)))
        os.remove(f"files/{user}/config/temp.png")

        imgLabel = Label(display)
        imgLabel.place(x=0, y=325)
        imgLabel.image = img
        imgLabel['image'] = imgLabel.image

        Label(display, text="Two-Factor Authentication", font=('arial', 30)).place(x=10, y=140)
        Label(display, text="Scan this QR code\nIn your authenticator app", font=('arial', 20)).place(x=25, y=280)
        otpText = Label(display, text=otpT, font=('arial', 20))
        otpText.place(x=15, y=200)
        activeOTP = Button(display, text=data, font=('arial', 25), command=lambda:active())
        activeOTP.place(x=500, y=140, height=50, width=80)
    
    Label(controls, text="Settings", font=('arial', 40), bg="#4a4a4a").place(x=380, y=10)

    Button(controls, text="Change Password", font=('arial', 20), command=changePWD).place(x=10, y=10, height=50, width=230)
    Button(controls, text="Delete Account",  font=('arial', 20), command=deleteACC).place(x=10, y=70, height=50, width=230)
    Button(controls, text="2 FA",  font=('arial', 20), command=otp).place(x=776, y=10, height=50, width=230)
