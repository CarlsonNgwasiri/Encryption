from cryptography.fernet import Fernet

fkey = open("file_key.txt",'rb')
key = fkey.read()
cipher = Fernet(key)

encrypted_text = cipher.encrypt(b'Prof Tonye is my teacher')
print(encrypted_text)
