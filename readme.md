# Tutorials

- http://zetcode.com/gui/pyqt5/

# Setup

## Windows 7 (x64)

### Python 3.5.2 (x64) + PyQt5 for Python 3.5 (x64)

#### Python
- File `python-3.5.2-amd64.exe`
- Source https://www.python.org/downloads/release/python-352/

#### PyQt5
- File `PyQt5-5.6-gpl-Py3.5-Qt5.6.0-x64-2.exe`
- Source https://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.6/

#### cx_Freeze
- Not yet available for Python 3.5
- Discussion https://sourceforge.net/p/cx-freeze/mailman/message/34695906/

### Python 3.4.4 (x64) + PyQt5 for Python 3.4 (x64)

#### Python
- File `python-3.4.4-amd64.exe`
- Source https://www.python.org/downloads/release/python-344/
- Latest available version that provides a Windows installer

#### PyQt5
- File `PyQt5-5.5.1-gpl-Py3.4-Qt5.5.1-x64.exe`
- Source https://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.5.1/
- Latest available version that supports Python 3.4

#### cx_Freeze + Microsoft Visual CPP Build Tools
- Source http://landinghub.visualstudio.com/visual-cpp-build-tools
- Command `pip install cx_Freeze`

### Notes
- Nothing else is required
- Also see http://stackoverflow.com/a/38404201

## Debian Linux

#### Python
- Should already be installed: `which python3`
- `pip` however might not be: `sudo apt-get install python3-pip`
- Then update `pip` to the latest version: `sudo pip3 install --upgrade pip`

#### PyQt5
- `pip install pyqt5` for use or `sudo pip install pyqt5` for system wide installation of module

### Notes
- Running `python main.py` will not work because the installed 2.x version is used, and this lacks the `pyqt5` module
- Run `python3 main.py` instead
