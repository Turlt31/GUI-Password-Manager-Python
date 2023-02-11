from cryption import encryptpsw, make_key
from tkinter import *
import tkinter.font as tkFont
import apps
import os

root = Tk()
root.title("Password Manager")
root.geometry("1266x668")
root.resizable(False, False)
root.configure(bg="#303030")

rect = Canvas(root, width=500, height=250, bg="white", highlightthickness=0)
rect.place(relx=0.5, rely=0.5, anchor=CENTER)
#rect.create_rectangle(0, 0, 600, 300, outline="black", width=10)

def clearScreen(a):
    if a == "ro":
        for widget in root.winfo_children():
                widget.destroy()
    elif a == "re":
        for widget in rect.winfo_children():
                widget.destroy()

def main(user):
    clearScreen("ro")
    menu = Canvas(root, width=250, height=668, bg="#303030", highlightthickness=0)
    menu.place(x=0, y=0)


    displayFrame = Frame(root, bg="blue")
    displayFrame.place(x=250, y=0, width=1016, height=1000)

    display = Canvas(displayFrame, bg="white", highlightthickness=0)
    display.place(x=0, y=0, width=1016, height=1000)

    scrollbar = Scrollbar(displayFrame, orient='vertical', command=display.yview)
    scrollbar.place(x=1000, y=130, width=20, height=540)

    display.configure(yscrollcommand=scrollbar.set)
    display.bind('<Configure>', lambda e: display.configure(scrollregion=display.bbox("all")))

    frame = Frame(display, width=1000, height=10000, bg="white")
    display.create_window((0,0), window=frame, anchor="nw")

    controls = Canvas(root, width=1016, height=130, bg="#4a4a4a", highlightthickness=0)
    controls.place(x=250, y=0)

    Label(menu, text=f"Hello {user}!", font=("arial", 32), bg="#303030", fg="white").place(x=5, y=10)

    Button(menu, text="Passwords", font=("arial", 25), command=lambda:apps.password(frame, controls, user)).place(x=10, y=150, height=50, width=230)
    Button(menu, text="Cards"    , font=("arial", 25), command=lambda:apps.card(frame, controls, user)    ).place(x=10, y=210, height=50, width=230)
    Button(menu, text="Settings" , font=("arial", 25), command=lambda:apps.settings(display, controls, user)).place(x=10, y=610, height=50, width=230)
    #Button(menu, text="Logout"   , font=("arial", 25), command=lambda:apps.logout())

def login():
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
            Label(rect, text="Account Created!", font=('arial', 25), bg="grey").place(x=185, y=130)
        def returnB():
            clearScreen("re")
            login()
        clearScreen("re")
        Label(rect, text="Username:", bg="grey", font=("arial", 26)).place(x=20, y=20)
        Label(rect, text="Password:", bg="grey", font=("arial", 26)).place(x=20, y=70)

        u = Entry(rect, font=("arial", 18))
        u.place(x=200, y=30, width=200, height=35)
        p = Entry(rect, font=("arial", 18), show="●")
        p.place(x=200, y=80, width=200, height=35)

        Button(rect, text="Register", font=("arial", 28), command=addToFile).place(x=20, y=130, height=60, width=150)
        Button(rect, text="Back", font=('arial', 28), command=returnB).place(x=385, y=200, height=45, width=110)

    welcome = tkFont.Font(family="arial", size=30, weight="bold")

    Label(rect,text="Please Login", bg="white", font=welcome).place(x=125, y=15)
    Label(rect, text="Username:", bg="white", font=("arial", 26)).place(x=40, y=70)
    Label(rect, text="Password:", bg="white", font=("arial", 26)).place(x=40, y=120)

    u = Entry(rect, font=("arial", 18))
    u.place(x=220, y=80, width=200, height=35)
    p = Entry(rect, font=("arial", 18), show="●")
    p.place(x=220, y=130, width=200, height=35)

    Button(rect, text="Login", font=("arial", 30), command=checkLogin).place(x=60, y=180, height=60, width=150)
    Button(rect, text="Register", font=("arial", 28), command=register).place(x=300, y=180, height=60, width=150)

#main("a")
login()

root.mainloop()
