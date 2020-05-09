from ui import config
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtWidgets


def show_msg_wrong_input():
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Information)
    msg.setWindowIcon(QIcon('icons/bombucha.png'))
    msg.setWindowTitle(config.items_text['msg_wrong_input_window_title'])
    msg.setText(config.items_text['msg_wrong_input_text'])
    msg.setFont(config.mainfont)
    msg.setStyleSheet(config.colors['centralWidget'])

    msg.exec()


def show_msg_exelsaved():
    msg = QtWidgets.QMessageBox()
    msg.setIconPixmap(QPixmap('icons/symbol_ok.png'))
    msg.setWindowIcon(QIcon('icons/bombucha.png'))
    msg.setWindowTitle(config.items_text['msg_exelsaved_window_title'])
    msg.setText(config.items_text['msg_exelsaved_text'])
    msg.setFont(config.bigfont)
    msg.setStyleSheet(config.colors['centralWidget'])

    msg.exec()
