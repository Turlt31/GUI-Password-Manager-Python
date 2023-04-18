# GUI-Password-Manager

Can safely store:
  1. Passwords, Usernames
  2. Credit/Debit cards

Encryption:
  * Sha256 for the Master password
  * Cryptograpy.fernet for the accounts

Features:
  * Account system
  * Two-Factor Authentication
  * Scroll bar (Im really exited about it lmoa)

For a .exe version run the following commands in the same directory as the .py file  
```
pip install pyinstaller
pyinstaller --onefile -w main.py
```
After that 2 new folders will apear in the same directory  
You can safely delete "build"   
And in "dist" will be the .exe file  
Move the .exe file in to the same directory where the .py file is
