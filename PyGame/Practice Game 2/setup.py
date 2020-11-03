import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
               Executable('Shooter.pyw',
                          icon="Images\\gps.ico",
                          base=base)
]
includefiles = ['Sound Effects','Music','Fonts','Images']

setup(name='Shooter',
      version='3.0',
      description='GUI Shooter',
      author = "Abbacus Inc.",
      options = {'build_exe': {'include_files':includefiles}},
      executables=executables
      )


#run with " py setup.py build "
