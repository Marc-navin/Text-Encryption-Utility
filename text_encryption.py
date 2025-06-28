import ast
from cryptography.fernet import Fernet
import os

k=Fernet.generate_key()
if not os.path.exists("key.key"): #to create an key if it not exists
    with open("key.key", "wb") as f:
        f.write(Fernet.generate_key())

with open('key.key','rb') as f:
    key=f.read()
    cipher=Fernet(key)
    while True:
        print('Enter 1 to encrypt')
        print('Enter 2 to decrypt')
        try:
            ch = int(input('Enter your choice: '))
        except ValueError:
            print(" Invalid input. Please enter 1 or 2.\n")
            continue
        message=input('Enter a message:')
        if ch==1:
            ciphertext=cipher.encrypt(message.encode())
            print('Encrypted message :',ciphertext,'\n')
        elif ch==2:
            ciphertext = ast.literal_eval(message)  #For converting safely to bytes
            decrypted = cipher.decrypt(ciphertext).decode()
            print('Decrypted message :',decrypted,'\n')
        else:
            print('Invalid choice ! Enter a valid choice\n')
        print('\n------------------------------------------------------------------------------------------------------------------\n')
