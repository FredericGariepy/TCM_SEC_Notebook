'''
Convert Python scripts into standalone executable Windows programs (EXE files).
Allows Python programs to be run on Windows systems without requiring a Python interpreter.

'''

from distutils.core import setup
import py2exe

setup(
    options={
        'py2exe': {
            'bundle_files': 1,  # Bundle everything into a single file
            'compressed': True,  # Compress the library archive
        }
    },
    windows=[{'script': 'hello.py'}], # Specify the script to convert
    zipfile=None,  # No separate zip file
)
