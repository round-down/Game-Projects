import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
               Executable('main.pyw',
                          icon="Images\\",
                          base=base)
]
Packages=['settings']# add more .py files that the main needs to run
includefiles = ['Sound Effects','Music','Fonts','Images']

setup(name='',
      version='1.0',
      description='GUI',
      author = "Abbacus Inc.",
      options = {'build_exe': {'packages':Packages,'include_files':includefiles}},
      executables=executables
      )


#run with " py setup.py build "
