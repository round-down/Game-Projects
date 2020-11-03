import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
               Executable('main.pyw',
                          icon="Images\\bunny.ico",
                          base=base)
]
Packages=['settings','sprites']# add more .py files that the main needs to run
includefiles = ['Sound Effects','Music','Fonts','Images']

setup(name='Platformer',
      version='1.0',
      description='GUI Platformer',
      author = "Abbacus Inc.",
      options = {'build_exe': {'packages':Packages,'include_files':includefiles}},
      executables=executables
      )


#run with " python setup.py build "
