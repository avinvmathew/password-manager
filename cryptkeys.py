import os
import keyring

from cryptography.fernet import Fernet

key_file_path = "key.key"
class CryptKeys:
    def __init__(self):
        if not os.path.exists(key_file_path):
            self.key = Fernet.generate_key()
            # with open("key.key", "wb") as key_file:
            #     key_file.write(self.key)
            keyring.set_password("password_manager", "encryption_key", self.key.decode())
            print("Key stored in keyring.")

    def load_key(self):
        # with open("key.key", "rb") as key_file:
        #     return key_file.read()
        key_str = keyring.get_password("password_manager", "encryption_key")
        if not key_str:
            raise ValueError("Encryption key not found in keyring.")
        return key_str.encode()

    def encrypt_password(self,password):
        key = self.load_key()
        f = Fernet(key)
        encrypted = f.encrypt(password.encode())
        return encrypted.decode()  # store as string in JSON

    def decrypt_password(self,encrypted_password):
        key = self.load_key()
        f = Fernet(key)
        decrypted = f.decrypt(encrypted_password.encode())
        return decrypted.decode()
