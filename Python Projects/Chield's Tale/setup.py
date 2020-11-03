import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Console'#'Win32GUI' use if GUI

executables = [
               Executable('Chield\'s Tale.py',
                          icon="Images\\pt.ico",
                          base=base)
]
Packages=['game']# add more .py files that the main needs to run
includefiles = ['Music','Sound Effects','Images']

setup(name='Chield\'s Tale',
      version='5.0',
      description='Console Quest',
      author = "Abbacus Inc.",
      options = {'build_exe': {'packages':Packages,'include_files':includefiles}},
      executables=executables
      )

# run with " python setup.py build "
