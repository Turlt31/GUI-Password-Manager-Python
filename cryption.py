from cryptography.fernet import Fernet
from hashlib import sha256
import base64
import pyotp
import json

def get_key(user):
	with open(f'files/{user}/config/key.key', 'rb') as f:
		return f.read()
def make_key(user):
	key = Fernet.generate_key()
	with open(f"files/{user}/config/key.key", 'wb') as f:
		f.write(key)

	key = pyotp.random_base32()
	with open(f"files/{user}/config/otp.json", 'r') as f:
		data = json.load(f)
	with open(f"files/{user}/config/otp.json", 'w') as f:
		json.dump({'active':data['active'], 'key':key}, f)


def encryptPWD(name, site, user, pasw):
	encryptedS, encryptedU, encryptedP = "", "", ""
	key = get_key(name)

	for letter in site:
		if letter == ' ':
			encryptedS += ' '
		else:
			encryptedS += chr(ord(letter) + 5)
	for letter in user:
		if letter == ' ':
			encryptedU += ' '
		else:
			encryptedU += chr(ord(letter) + 5)
	for letter in pasw:
		if letter == ' ':
			encryptedP += ' '
		else:
			encryptedP += chr(ord(letter) + 5) 
	return Fernet(key).encrypt(encryptedS.encode()).decode(), Fernet(key).encrypt(encryptedU.encode()).decode(), Fernet(key).encrypt(encryptedP.encode()).decode()
def decryptPWD(name, site, user, pasw):
	decryptedS, decryptedU, decryptedP = "", "", ""
	key = get_key(name)

	site, user, pasw = Fernet(key).decrypt(site.encode()).decode(), Fernet(key).decrypt(user.encode()).decode(), Fernet(key).decrypt(pasw.encode()).decode()	
	for letter in site:
		if letter == ' ':
			decryptedS += ' '
		else:
			decryptedS += chr(ord(letter) - 5)
	for letter in user:
		if letter == ' ':
			decryptedU += ' '
		else:
			decryptedU += chr(ord(letter) - 5)
	for letter in pasw:
		if letter == ' ':
			decryptedP += ' '
		else:
			decryptedP += chr(ord(letter) - 5) 
	return decryptedS, decryptedU, decryptedP

def encryptCRD(user, name, num, date, ccv):
	encryptedN, encryptedNU, encryptedD, encryptedC = "", "", "", ""
	key = get_key(user)

	for letter in name:
		if letter == ' ':
			encryptedN += ' '
		else:
			encryptedN += chr(ord(letter) + 5)
	for letter in num:
		if letter == ' ':
			encryptedNU += ' '
		else:
			encryptedNU += chr(ord(letter) + 5)
	for letter in date:
		if letter == ' ':
			encryptedD += ' '
		else:
			encryptedD += chr(ord(letter) + 5)
	for letter in ccv:
		if letter == ' ':
			encryptedC += ' '
		else:
			encryptedC += chr(ord(letter) + 5) 
	return Fernet(key).encrypt(encryptedN.encode()).decode(), Fernet(key).encrypt(encryptedNU.encode()).decode(), Fernet(key).encrypt(encryptedD.encode()).decode(), Fernet(key).encrypt(encryptedC.encode()).decode()
def decryptCRD(user, name, num, date, ccv):
	decryptedN, decryptedNU, decryptedD, decryptedC = "", "", "", ""
	key = get_key(user)

	name, num, date, ccv = Fernet(key).decrypt(name.encode()).decode(), Fernet(key).decrypt(num.encode()).decode(), Fernet(key).decrypt(date.encode()).decode(), Fernet(key).decrypt(ccv.encode()).decode()	
	for letter in name:
		if letter == ' ':
			decryptedN += ' '
		else:
			decryptedN += chr(ord(letter) - 5)
	for letter in num:
		if letter == ' ':
			decryptedNU += ' '
		else:
			decryptedNU += chr(ord(letter) - 5)
	for letter in date:
		if letter == ' ':
			decryptedD += ' '
		else:
			decryptedD += chr(ord(letter) - 5)
	for letter in ccv:
		if letter == ' ':
			decryptedC += ' '
		else:
			decryptedC += chr(ord(letter) - 5) 
	return decryptedN, decryptedNU, decryptedD, decryptedC

def encryptCRO(user, addr, priv, name):
	encryptedA, encryptedP, encryptedN = "", "", ""
	key = get_key(user)	

	for letter in addr:
		if letter == " ":
			encryptedA += " "
		else:
			encryptedA += chr(ord(letter) + 5)
	for letter in priv:
		if letter == " ":
			encryptedP += " "
		else:
			encryptedP += chr(ord(letter) + 5)
	for letter in name:
		if letter == " ":
			encryptedN += " "
		else:
			encryptedN += chr(ord(letter) + 5)
	return Fernet(key).encrypt(encryptedA.encode()).decode(), Fernet(key).encrypt(encryptedP.encode()).decode(), Fernet(key).encrypt(encryptedN.encode()).decode()
def decryptCRO(user, addr, priv, name):
	decryptedA, decryptedP, decryptedN = "", "", ""
	key = get_key(user)	

	addr, priv, name = Fernet(key).decrypt(addr.encode()).decode(), Fernet(key).decrypt(priv.encode()).decode(), Fernet(key).decrypt(name.encode()).decode()
	for letter in addr:
		if letter == " ":
			decryptedA += " "
		else:
			decryptedA += chr(ord(letter) - 5)
	for letter in priv:
		if letter == " ":
			decryptedP += " "
		else:
			decryptedP += chr(ord(letter) - 5)
	for letter in name:
		if letter == " ":
			decryptedN += " "
		else:
			decryptedN += chr(ord(letter) - 5)
	return decryptedA, decryptedP, decryptedN

def encryptpsw(pasw):
	encryptedP = ""
	for letter in pasw:
		if letter == ' ':
			encryptedP += ' '
		else:
			encryptedP += chr(ord(letter) + 5)
	return sha256(bytes(encryptedP, 'utf-8')).hexdigest()
