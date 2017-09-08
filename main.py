#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QPushButton, QWidget
from PyQt5.QtGui import QIcon
# from PyQt5.QtWidgets import QTextEdit


class ButtonWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.setAcceptDrops(True)

        btn = QPushButton('Click', self)
        btn.resize(btn.sizeHint())
        btn.move(10, 20)
        btn.clicked.connect(self.print_something)

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('FileName'):
            self.parent.statusBar().showMessage('Ready to drop ...')
            e.accept()
        else:
            self.parent.statusBar().showMessage('Unsupported object ...')
            e.ignore()

    def dragLeaveEvent(self, e):
        # Doesn't fire on leave of ignored object, so the "unsupported object" message never disappears. Workaround?
        self.parent.statusBar().showMessage('')

    def dragMoveEvent(self, e):
        # Not really useful when using drag and drop with files/folders.
        pass

    def dropEvent(self, e):
        self.parent.statusBar().showMessage('Dropped')
        print(e.mimeData().text())

    def print_something(self):
        self.parent.statusBar().showMessage('Something')


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 200, 300, 400)  # move and resize
        self.setWindowTitle('Hello World')
        self.setWindowIcon(QIcon('blocks.png'))

        button_widget = ButtonWidget(self)
        self.setCentralWidget(button_widget)

        exit_action = QAction(QIcon('exit.png'), 'Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(self.close)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(exit_action)

        tool_bar = self.addToolBar('Exit')
        tool_bar.addAction(exit_action)

        self.statusBar().showMessage('Ready')

        self.show()


def process_cl_args():
    # Source: http://stackoverflow.com/questions/11713006/elegant-command-line-argument-parsing-for-pyqt
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--swallow', action='store')  # optional flag
    parser.add_argument('-t', '--top', action='store')  # optional flag
    parser.add_argument('holy_hand_grenade', action='store')  # positional argument

    parsed, unparsed = parser.parse_known_args()
    return parsed, unparsed


if __name__ == '__main__':
    if len(sys.argv) > 1:
        parsed_args, unparsed_args = process_cl_args()
    else:
        parsed_args = None
        unparsed_args = []
    qt_args = sys.argv[:1] + unparsed_args

    print(parsed_args)  # Namespace(holy_hand_grenade='True', swallow='opt2', top=None)
    print(unparsed_args)  # ['something_else']

    app = QApplication(qt_args)  # QApplication expects the first argument to be the program name
    ex = Example()
    ex.show()
    exit_code = app.exec_()
    sys.exit(exit_code)

# Command:
# C:\Python34\python.exe main.py True -s opt2 something_else
# C:\Python35\python.exe main.py True -s opt2 something_else
