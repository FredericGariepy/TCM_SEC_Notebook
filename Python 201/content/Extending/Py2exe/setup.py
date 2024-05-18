'''
Convert Python scripts into standalone executable Windows programs (EXE files).
Allows Python programs to be run on Windows systems without requiring a Python interpreter.

'''
from py2exe import freeze
freeze(
  console = [{'script':'hello.py'}], # Specify the script to convert
  options = {
      'py2exe': {
          'bundle_files': 1,  # Bundle everything into a single file
          'compressed' : True # Compress the library archive
      }
    },
    zipfile = None # No separate zip file
)
