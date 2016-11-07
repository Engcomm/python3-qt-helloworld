#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QPushButton, QWidget
from PyQt5.QtGui import QIcon


class ButtonWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        btn = QPushButton('Click', self)
        btn.resize(btn.sizeHint())
        btn.move(10, 20)
        btn.clicked.connect(self.print_something)

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

        #text_edit_widget = QTextEdit()
        #self.setCentralWidget(text_edit_widget)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)  # pass optional command line arguments through
    ex = Example()
    sys.exit(app.exec_())
