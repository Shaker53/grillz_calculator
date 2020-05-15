from ui import config
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtWidgets


def show_msg_not_all_important_params():
    question_msg = QtWidgets.QMessageBox()
    question_msg.setIcon(QtWidgets.QMessageBox.Information)
    question_msg.setWindowTitle(config.items_text['msg_not_all_important_params_window_title'])
    question_msg.setWindowIcon(QIcon('images/icons/bombucha.png'))
    question_msg.setText(config.items_text['msg_not_all_important_params_text'])

    question_msg.setFont(config.mainfont)
    question_msg.setStyleSheet(config.colors['centralWidget'])
    button_ok = question_msg.addButton(config.items_text['msg_not_all_important_params_button_ok'],
                                       QtWidgets.QMessageBox.AcceptRole)
    button_ok.setFont(config.littlefont)
    button_no = question_msg.addButton(config.items_text['msg_not_all_important_params_button_no'],
                                       QtWidgets.QMessageBox.RejectRole)
    button_no.setFont(config.littlefont)
    question_msg.exec()
    if question_msg.clickedButton() == button_ok:
        return 'back_button_pushed'
    else:
        return 'forward'


def show_msg_wrong_input():
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Information)
    msg.setWindowIcon(QIcon('images/icons/bombucha.png'))
    msg.setWindowTitle(config.items_text['msg_wrong_input_window_title'])
    msg.setText(config.items_text['msg_wrong_input_text'])
    msg.setFont(config.mainfont)
    msg.setStyleSheet(config.colors['centralWidget'])

    msg.exec()


def show_msg_exelsaved():
    msg = QtWidgets.QMessageBox()
    msg.setIconPixmap(QPixmap('images/icons/symbol_ok.png'))
    msg.setWindowIcon(QIcon('images/icons/bombucha.png'))
    msg.setWindowTitle(config.items_text['msg_exelsaved_window_title'])
    msg.setText(config.items_text['msg_exelsaved_text'])
    msg.setFont(config.bigfont)
    msg.setStyleSheet(config.colors['centralWidget'])

    msg.exec()
