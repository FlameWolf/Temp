import os
import base64
from cryptography.fernet import Fernet

class CompiledEncryptor:
    # Generate and use a static key
    ENCRYPTION_KEY = b'2A4cD5H-9n-y2SrQRT3UZ9cPaZFo5a0iAdRQeT7ZnUw='  # Replace with actual key

    @classmethod
    def generate_key(cls):
        """Generate a new encryption key"""
        key = Fernet.generate_key()
        print(f"Generated encryption key: {key}")
        print("Update ENCRYPTION_KEY in both encrypt_compiled.py and runtime_loader.py")
        return key

    @classmethod
    def encrypt_file(cls, file_path: str, output_path: str = None):
        """Encrypt a compiled extension file"""
        if output_path is None:
            output_path = file_path + '.encrypted'

        # Read the compiled file
        with open(file_path, 'rb') as f:
            data = f.read()

        # Encrypt the data
        fernet = Fernet(cls.ENCRYPTION_KEY)
        encrypted_data = fernet.encrypt(data)

        # Save encrypted file
        with open(output_path, 'wb') as f:
            f.write(encrypted_data)

        print(f"File encrypted successfully: {output_path}")
        return output_path

if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        choice = input("1. Generate new key\n2. Encrypt compiled file\nChoose (1/2): ")

        if choice == "1":
            CompiledEncryptor.generate_key()
        elif choice == "2":
            compiled_file = input("Enter path to compiled file (.pyd/.so): ")
            if os.path.exists(compiled_file):
                CompiledEncryptor.encrypt_file(compiled_file)
            else:
                print("File not found!")
    elif len(sys.argv) == 2:
        # Direct file encryption
        compiled_file = sys.argv[1]
        if os.path.exists(compiled_file):
            CompiledEncryptor.encrypt_file(compiled_file)
        else:
            print("File not found!")