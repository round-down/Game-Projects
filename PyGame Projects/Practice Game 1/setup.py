import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
               Executable('testpygame.py',
                          icon="Images\\ph34.ico",
                          base=base)
]
includefiles = ['Sound Effects','Music','Fonts','Images']

setup(name='Chield\'s Tale',
      version='1.0',
      description='GUI Quest',
      author = "Abbacus Inc.",
      options = {'build_exe': {'include_files':includefiles}},
      executables=executables
      )


#run with " py setup.py build "
