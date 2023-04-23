from cryption import encryptpsw, make_key
from tkinter import *
import tkinter.font as tkFont
import pyotp
import json
import apps
import os

root = Tk()
root.title("Password Manager")
root.geometry("1266x668")
root.resizable(False, False)
root.configure(bg="#303030")
root.iconbitmap('icon/pwm.ico')

def main(user):
    for widget in root.winfo_children(): widget.destroy
        
    menu = Canvas(root, width=250, height=668, bg="#303030", highlightthickness=0)
    menu.place(x=0, y=0)

    def scroll_canvas(event):
        if event.delta:
            display.yview_scroll(-1 * int(event.delta/120), "units")
        else:
            if event.num == 5:
                display.yview_scroll(1, "units")
            else:
                display.yview_scroll(-1, "units")

    display = Canvas(root, scrollregion=(0,0,1000,2000))
    display.place(x=250, y=130, width=1016, height=700)

    displayFrame = Frame(display, width=1016, height=2000)

    vscroll = Scrollbar(root, orient="vertical", command=display.yview)
    vscroll.place(x=1265, y=130, height=535, anchor="ne")
    display.configure(yscrollcommand=vscroll.set, xscrollcommand=None)
    display.create_window((0, 0), window=displayFrame, anchor='nw')
    display.bind_all("<MouseWheel>", scroll_canvas)

    controls = Canvas(root, width=1016, height=130, bg="#4a4a4a", highlightthickness=0)
    controls.place(x=250, y=0)

    Label(menu, text=f"Hello {user}!", font=("arial", 32), bg="#303030", fg="white").place(x=5, y=10)

    Button(menu, text="Password",  font=("arial", 25), command=lambda:apps.password(displayFrame, controls, user)).place(x=10, y=130, height=50, width=230)
    Button(menu, text="Card"    ,  font=("arial", 25), command=lambda:apps.card(displayFrame, controls, user)    ).place(x=10, y=190, height=50, width=230)
    Button(menu, text="Notes"   ,  font=("arial", 25), command=lambda:apps.notes(displayFrame, controls, user)   ).place(x=10, y=250, height=50, width=230)
    Button(menu, text="Settings" , font=("arial", 25), command=lambda:apps.settings(displayFrame, controls, user)).place(x=10, y=610, height=50, width=230)
    Button(menu, text="Logout"   , font=("arial", 25), command=loginScreen).place(x=10, y=550, height=50, width=230)
    apps.password(displayFrame, controls, user)

def loginScreen():
    for widget in root.winfo_children(): widget.destroy()
        
    def login():
        def otp():
            def on_return(event): authenticate()
            def authenticate():
                with open(f"files/{user}/config/otp.json", 'r') as f: data = json.load(f) 
                totp = pyotp.TOTP(data['key'])
                if totp.verify(code.get()): main(user.strip('\n')); otpS.destroy()
                else: pass
                
            otpS = Toplevel(root)
            otpS.title("2 Factor Authentication")
            otpS.geometry("500x200")
            otpS.resizable(False, False)
            
            Label(otpS, text="2 Factor Authentication", font=('arial', 25)).place(x=80,y=10)
            Label(otpS, text="Code", font=('arial', 20)).place(x=15, y=70)
            code = Entry(otpS, font=('arial', 20))
            code.place(x=100, y=73, height=35, width=200)
            code.bind("<Return>", on_return)
            Button(otpS, text="Authenticate", font=('arial', 20), command=authenticate).place(x=310, y=73, height=35, width=180)

        user = u.get()
        pswd = encryptpsw(p.get())

        e = Label(root, font=('arial', 25), bg="#303030", fg="#f70a22")
        e.place(x=385, y=470)

        with open(f'files/login.txt', 'r') as f:
            logins =  f.readlines()
        for i in logins:
            i = i.split(',')
            if pswd == i[0] and user == i[1].strip('\n'):
                with open(f'files/{user}/config/otp.json', 'r') as f: data = json.load(f)
                otpON = data['active']

                if otpON: otp(); e.destroy()
                else: main(user.strip('\n')); e.destroy()
            elif pswd == [0] or user == i[1].strip('\n'): e.config(text="Error: Incorrect Password or Username")
            else: e.config(text="Error: Account does not exist")
    def register():
        def addToFile():
            username = u.get()
            password = p.get()

            os.mkdir(f"files/{username}")
            os.mkdir(f"files/{username}/config")

            with open('files/login.txt', 'a') as f: f.write(f"{encryptpsw(password)},{username}\n")

            [open(f"files/{username}/{file}", 'w').close() for file in ["card.txt", "password.txt", "notes.txt"]]
            [open(f"files/{username}/config/{file}", 'w').close() for file in ["otp.json"]]

            with open(f'files/{username}/config/otp.json', 'w') as f: json.dump({"active":False, "key":""}, f)
            make_key(username)

            Label(rect, text="Account Created!", font=('arial', 25), bg="white").place(x=185, y=130)
        def returnB():
            for widget in rect.winfo_children():widget.destroy()
            loginScreen()
        for widget in rect.winfo_children():
                widget.destroy()
        Label(rect, text="Username:", bg="white", font=("arial", 26)).place(x=20, y=20)
        Label(rect, text="Password:", bg="white", font=("arial", 26)).place(x=20, y=70)

        u = Entry(rect, font=("arial", 18))
        u.place(x=200, y=30, width=200, height=35)
        p = Entry(rect, font=("arial", 18), show="●")
        p.place(x=200, y=80, width=200, height=35)

        Button(rect, text="Register", font=("arial", 28), command=addToFile).place(x=20, y=130, height=60, width=150)
        Button(rect, text="Back", font=('arial', 28), command=returnB).place(x=375, y=190, height=45, width=110)
    def on_return(event): login()
    rect = Canvas(root, width=500, height=250, bg="white", highlightthickness=0)
    rect.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    rect.create_line(0, 0, 0, 250, fill="black", width=10)
    rect.create_line(0, 0, 500, 0, fill="black", width=10)
    rect.create_line(500, 0, 500, 250, fill="black", width=10)
    rect.create_line(0, 250, 500, 250, fill="black", width=10)

    welcome = tkFont.Font(family="arial", size=30, weight="bold")

    Label(rect,text="Please Login", bg="white", font=welcome).place(x=125, y=15)
    Label(rect, text="Username:", bg="white", font=("arial", 26)).place(x=40, y=70)
    Label(rect, text="Password:", bg="white", font=("arial", 26)).place(x=40, y=120)

    u = Entry(rect, font=("arial", 18))
    u.place(x=220, y=80, width=200, height=35)
    p = Entry(rect, font=("arial", 18), show="●")
    p.place(x=220, y=130, width=200, height=35)

    p.bind("<Return>", on_return)
    Button(rect, text="Login", font=("arial", 30), command=login).place(x=60, y=180, height=60, width=150)
    Button(rect, text="Register", font=("arial", 28), command=register).place(x=300, y=180, height=60, width=150)

loginScreen()

root.mainloop()
