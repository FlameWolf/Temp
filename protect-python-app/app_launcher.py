#!/usr/bin/env python3
import sys
import os
from runtime_loader import CythonRuntimeLoader

# Embedded encrypted application data
ENCRYPTED_APP_NAME = "app.encrypted"  # Update this

def main():
    # Check if encrypted file exists
    if not os.path.exists(ENCRYPTED_APP_NAME):
        print(f"Encrypted application not found: {ENCRYPTED_APP_NAME}")
        sys.exit(1)

    # Load and run the encrypted application
    loader = CythonRuntimeLoader(ENCRYPTED_APP_NAME)
    loader.load_and_run()

if __name__ == "__main__":
    main()