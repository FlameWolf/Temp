import os
import sys
import shutil
from cythonize_app import compile_to_cython
from encrypt_compiled import CompiledEncryptor

def build_encrypted_application(source_file: str, cleanup: bool = True):
    """Complete build process: Python -> Cython -> Encrypt"""

    print(f"Building encrypted application from: {source_file}")

    # Step 1: Compile to Cython
    print("\n=== Step 1: Compiling with Cython ===")
    compiled_file = compile_to_cython(source_file)

    if not compiled_file:
        print("Failed to compile with Cython!")
        return False

    # Step 2: Encrypt the compiled file
    print("\n=== Step 2: Encrypting compiled extension ===")
    encrypted_file = CompiledEncryptor.encrypt_file(compiled_file)

    # Step 3: Copy encrypted file to main directory
    final_name = os.path.splitext(os.path.basename(source_file))[0] + ".encrypted"
    final_path = os.path.join(os.getcwd(), final_name)
    shutil.copy2(encrypted_file, final_path)

    print(f"\n=== Build Complete ===")
    print(f"Encrypted application: {final_path}")
    print(f"Run with: python runtime_loader.py {final_name}")

    # Cleanup build directory
    if cleanup:
        try:
            shutil.rmtree("build")
            print("Build directory cleaned up.")
        except:
            pass

    return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python build_encrypted_app.py <python_file>")
        print("This will compile your Python file with Cython and encrypt it.")
        sys.exit(1)

    source_file = sys.argv[1]

    if not os.path.exists(source_file):
        print(f"Source file not found: {source_file}")
        sys.exit(1)

    success = build_encrypted_application(source_file)

    if not success:
        print("Build failed!")
        sys.exit(1)