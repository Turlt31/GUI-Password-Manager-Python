from cryptography.fernet import Fernet
from hashlib import sha256

def get_key():
	with open('files/key.key', 'rb') as f:
		return f.read()

def encryptPWD(site, user, pasw):
	encryptedS, encryptedU, encryptedP = "", "", ""
	key = get_key()

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


def decryptPWD(site, user, pasw):
	decryptedS, decryptedU, decryptedP = "", "", ""
	key = get_key()

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


def encryptCRD(name, num, date, ccv):
	encryptedN, encryptedNU, encryptedD, encryptedC = "", "", "", ""
	key = get_key()

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

def decryptCRD(name, num, date, ccv):
	decryptedN, decryptedNU, decryptedD, decryptedC = "", "", "", ""
	key = get_key()

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


def encryptpsw(pasw):
	encryptedP = ""
	key = get_key()
	for letter in pasw:
		if letter == ' ':
			encryptedP += ' '
		else:
			encryptedP += chr(ord(letter) + 5)
	return sha256(bytes(encryptedP, 'utf-8')).hexdigest()

print(encryptpsw("Test123"))

