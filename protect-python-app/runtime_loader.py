import os
import sys
import tempfile
import importlib.util
import importlib.machinery
from cryptography.fernet import Fernet

class CythonRuntimeLoader:
    # Same key as used in encryption
    DECRYPTION_KEY = b'2A4cD5H-9n-y2SrQRT3UZ9cPaZFo5a0iAdRQeT7ZnUw='  # Replace with actual key

    def __init__(self, encrypted_file_path: str, module_name: str = None):
        self.encrypted_file_path = encrypted_file_path
        self.module_name = module_name or os.path.splitext(os.path.basename(encrypted_file_path))[0]
        if self.module_name.endswith('.encrypted'):
            self.module_name = self.module_name[:-10]  # Remove .encrypted suffix

    def _decrypt_file(self) -> bytes:
        """Decrypt the encrypted compiled file"""
        with open(self.encrypted_file_path, 'rb') as f:
            encrypted_data = f.read()

        fernet = Fernet(self.DECRYPTION_KEY)

        try:
            decrypted_data = fernet.decrypt(encrypted_data)
            return decrypted_data
        except Exception as e:
            raise ValueError("Failed to decrypt file. Invalid encryption key.") from e

    def _get_extension_suffix(self):
        """Get the appropriate extension suffix for this platform"""
        if sys.platform == "win32":
            return ".pyd"
        else:
            return ".so"

    def load_and_run(self):
        """Decrypt the compiled extension and execute it"""
        try:
            # Decrypt the compiled extension
            decrypted_data = self._decrypt_file()

            # Create temporary file with correct extension
            suffix = self._get_extension_suffix()
            with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as temp_file:
                temp_file.write(decrypted_data)
                temp_file_path = temp_file.name

            try:
                # Load the extension module
                spec = importlib.util.spec_from_file_location(self.module_name, temp_file_path)
                if spec is None:
                    raise ImportError(f"Could not load spec for {temp_file_path}")

                module = importlib.util.module_from_spec(spec)

                # Add to sys.modules
                sys.modules[self.module_name] = module

                # Execute the module
                spec.loader.exec_module(module)

                # If the module has a main function or __main__ block, it should execute automatically
                # For modules with __main__ conditional, we need to set __name__
                if hasattr(module, '__name__'):
                    module.__name__ = '__main__'
                    # Re-execute to trigger __main__ block
                    spec.loader.exec_module(module)

                return module

            finally:
                # Clean up temporary file
                try:
                    os.unlink(temp_file_path)
                except:
                    pass

        except Exception as e:
            print(f"Error loading encrypted extension: {e}")
            sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python runtime_loader.py <encrypted_compiled_file>")
        sys.exit(1)

    encrypted_file = sys.argv[1]

    if not os.path.exists(encrypted_file):
        print(f"Encrypted file not found: {encrypted_file}")
        sys.exit(1)

    loader = CythonRuntimeLoader(encrypted_file)
    loader.load_and_run()

if __name__ == "__main__":
    main()