#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from cx_Freeze import setup, Executable

# GUI applications require a different base on Windows (the default is for a console application).
base = 'Win32GUI' if sys.platform == 'win32' else None
icon = 'icon.ico'  # has to be an ico file, not a png file!

executables = [Executable(script='main.py',
                          initScript=None,
                          base=base,
                          targetDir=None,
                          targetName='main.exe',
                          compress=True,
                          copyDependentFiles=True,
                          appendScriptToExe=False,
                          appendScriptToLibrary=False,
                          icon=icon)
]

# Dependencies are automatically detected, but it might need fine tuning.
packages = []
includes = []
excludes = ['Tkinter']
include_files = ['blocks.png', 'exit.png']
path = []
build_options = dict(packages=packages, includes=includes, excludes=excludes, include_files=include_files, path=path)

setup(name='Py3QtHello',
      version='1.2.3.4',
      description='The resulting *.exe from the wxPython Freezing Template.',
      author='Guenther Eberl',
      author_email='guenther@eberl.se',
      license='GNU GENERAL PUBLIC LICENSE, Version 2, June 1991',
      url='http://www.eberl.se/',
      options=dict(build_exe=build_options),
      executables=executables)

# C:\Python34\python.exe setup_cx_freeze.py build
