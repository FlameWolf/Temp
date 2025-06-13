import os
import sys
import shutil
import subprocess
from setuptools import setup, Extension
from Cython.Build import cythonize
from Cython.Compiler import Options

# Enable C line tracing for better debugging (optional)
Options.docstrings = False
Options.embed_pos_in_docstring = False

def compile_to_cython(source_file: str, output_dir: str = "../build"):
    """Compile Python file to Cython extension"""

    if not os.path.exists(source_file):
        raise FileNotFoundError(f"Source file not found: {source_file}")

    # Create build directory
    os.makedirs(output_dir, exist_ok=True)

    # Get base name without extension
    base_name = os.path.splitext(os.path.basename(source_file))[0]

    # Create setup script content
    setup_content = f'''
import sys
from setuptools import setup, Extension
from Cython.Build import cythonize
from Cython.Compiler import Options

# Disable docstrings to reduce file size
Options.docstrings = False

# Define the extension
extensions = [
    Extension(
        "{base_name}",
        ["{source_file}"],
        language_level=3,  # Use Python 3
    )
]

# Setup configuration
setup(
    name="{base_name}",
    ext_modules=cythonize(
        extensions,
        compiler_directives={{
            'language_level': 3,
            'embedsignature': False,
            'boundscheck': False,
            'wraparound': False,
            'initializedcheck': False,
            'nonecheck': False,
        }}
    ),
    zip_safe=False,
)
'''

    # Write setup script
    setup_file = os.path.join(output_dir, "setup_temp.py")
    with open(setup_file, 'w') as f:
        f.write(setup_content)

    # Copy source file to build directory
    source_copy = os.path.join(output_dir, os.path.basename(source_file))
    shutil.copy2(source_file, source_copy)

    try:
        # Run the compilation
        print("Compiling with Cython...")
        result = subprocess.run([
            sys.executable, setup_file,
            "build_ext", "--inplace"
        ],
        cwd=output_dir,
        capture_output=True,
        text=True
        )

        if result.returncode != 0:
            print("Compilation failed!")
            print("STDOUT:", result.stdout)
            print("STDERR:", result.stderr)
            return None

        print("Compilation successful!")

        # Find the compiled extension file
        for file in os.listdir(output_dir):
            if file.startswith(base_name) and (file.endswith('.pyd') or file.endswith('.so')):
                compiled_file = os.path.join(output_dir, file)
                print(f"Compiled extension: {compiled_file}")
                return compiled_file

        print("Could not find compiled extension file!")
        return None

    except Exception as e:
        print(f"Compilation error: {e}")
        return None

    finally:
        # Clean up temporary files
        try:
            os.remove(setup_file)
            os.remove(source_copy)
        except:
            pass

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python cythonize_app.py <python_file>")
        sys.exit(1)

    source_file = sys.argv[1]
    compiled_file = compile_to_cython(source_file)

    if compiled_file:
        print(f"Successfully compiled: {compiled_file}")
    else:
        print("Compilation failed!")
        sys.exit(1)