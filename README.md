# GUI-Password-Manager

Can safely store:
  1. Passwords, Usernames
  2. Credit/Debit cards
  3. Crypto Addreses, private keys, names

Encryption:
  * Sha256 for the Master password
  * Cryptograpy.fernet for the accounts

Has an account system that creates seperet folders for each account  
And a diffrent key for Encryption and Decryption


For a .exe version run the following commands  
```
pip install pyinstaller
pyinstaller --onefile -w main.py
```
After that 2 new folders will apear in the same directory  
You can safely delete "build"   
And in "dist" will be the .exe file  
Move the .exe file in to the same directory where the .py file is
