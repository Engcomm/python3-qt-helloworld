#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import datetime
import os
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
        btn = QPushButton('Click', self)
        btn.resize(btn.sizeHint())
        btn.move(10, 20)
        btn.clicked.connect(self.print_something)

    def print_something(self):
        self.parent.statusBar().showMessage('Something')


class Example(QMainWindow):
    def __init__(self, start_time, opts):
        super().__init__()
        self.init_ui()

        if opts:
            if opts.leftpane:
                self.load_left_pane(opts.leftpane)

        ready_time = datetime.datetime.now()
        print('Startup took %s' % (ready_time - start_time))

    def load_left_pane(self, left_pane_option):
        path_list = self.get_valid_path_list(left_pane_option.replace('"', ''))
        print(path_list)

        path_string = os.path.join(*path_list)
        all_content_list = os.listdir(path_string)
        only_dirs_list = [d for d in all_content_list if os.path.isdir(os.path.join(path_string, d))]
        only_files_list = [f for f in all_content_list if os.path.isfile(os.path.join(path_string, f))]

        print(all_content_list)
        print(only_dirs_list)
        print(only_files_list)

    @staticmethod
    def get_valid_path_list(input_path):
        """
        Confirm that the supplied input_path is actually existing and listable on the system by the current user.

        Return the same path converted to a list if it is.
        If it is not go a level up until it is and return that path as a list.
        If nothing exists or is listable return an empty list.

        :return: list
        """
        path_list = input_path.split('\\')

        # Sanitize path
        # TODO This works for Windows, unclear what is needed for Linux and macOS
        for n, dir_name in enumerate(path_list):
            path_list[n] = dir_name.replace(':', ':%s' % os.sep)

        output_list = []
        for n, dir_name in enumerate(path_list):
            current_path_list = path_list[:len(path_list) - n]
            current_path_string = os.path.join(*current_path_list)
            if os.path.isdir(current_path_string):
                output_list = current_path_list
                return output_list
        return output_list

    def init_ui(self):
        self.setGeometry(100, 200, 300, 400)  # move and resize
        self.setWindowTitle('Hello World')
        self.setWindowIcon(QIcon('blocks.png'))

        # text_edit_widget = QTextEdit()
        # self.setCentralWidget(text_edit_widget)

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
    parser.add_argument('-lp', '--leftpane', action='store')  # optional flag
    parser.add_argument('-rp', '--rightpane', action='store')  # optional flag
    parser.add_argument('holy_hand_grenade', action='store')  # positional argument

    parsed, unparsed = parser.parse_known_args()
    return parsed, unparsed


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    if len(sys.argv) > 1:
        parsed_args, unparsed_args = process_cl_args()
    else:
        parsed_args = None
        unparsed_args = []
    qt_args = sys.argv[:1] + unparsed_args

    # print(parsed_args)  # Namespace(holy_hand_grenade='True', swallow='opt2', top=None)
    # print(unparsed_args)  # ['something_else']

    app = QApplication(qt_args)  # QApplication expects the first argument to be the program name
    ex = Example(start_time, parsed_args)
    exit_code = app.exec_()
    sys.exit(exit_code)

# Command:
# C:\Python34\python.exe main.py True -s opt2 something_else --leftpane "C:\Program Files (x86)\Microsoft SDKs\NETCoreSDK\System.Diagnostics.FileVersionInfo\4.0.0-beta-23123\blah"
# C:\Python35\python.exe main.py True -s opt2 something_else --leftpane "C:\Program Files (x86)\Microsoft SDKs\NETCoreSDK\System.Diagnostics.FileVersionInfo\4.0.0-beta-23123\blah"
