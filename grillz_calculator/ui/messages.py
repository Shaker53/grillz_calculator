from config import ui_config
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtWidgets


def show_msg_not_all_important_params():
    question_msg = QtWidgets.QMessageBox()
    question_msg.setIcon(QtWidgets.QMessageBox.Information)
    question_msg.setWindowTitle(ui_config.items_text['msg_not_all_important_params_window_title'])
    question_msg.setWindowIcon(QIcon('resources/images/icons/bombucha.png'))
    question_msg.setText(ui_config.items_text['msg_not_all_important_params_text'])

    question_msg.setFont(ui_config.mainfont)
    question_msg.setStyleSheet(ui_config.colors['centralWidget'])
    button_ok = question_msg.addButton(ui_config.items_text['msg_not_all_important_params_button_ok'],
                                       QtWidgets.QMessageBox.AcceptRole)
    button_ok.setFont(ui_config.littlefont)
    button_no = question_msg.addButton(ui_config.items_text['msg_not_all_important_params_button_no'],
                                       QtWidgets.QMessageBox.RejectRole)
    button_no.setFont(ui_config.littlefont)
    question_msg.exec()
    if question_msg.clickedButton() == button_ok:
        return True
    else:
        return False


def show_msg_wrong_input():
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Information)
    msg.setWindowIcon(QIcon('resources/images/icons/bombucha.png'))
    msg.setWindowTitle(ui_config.items_text['msg_wrong_input_window_title'])
    msg.setText(ui_config.items_text['msg_wrong_input_text'])
    msg.setFont(ui_config.mainfont)
    msg.setStyleSheet(ui_config.colors['centralWidget'])

    msg.exec()


def show_msg_exelsaved():
    msg = QtWidgets.QMessageBox()
    msg.setIconPixmap(QPixmap('resources/images/icons/symbol_ok.png'))
    msg.setWindowIcon(QIcon('resources/images/icons/bombucha.png'))
    msg.setWindowTitle(ui_config.items_text['msg_exelsaved_window_title'])
    msg.setText(ui_config.items_text['msg_exelsaved_text'])
    msg.setFont(ui_config.bigfont)
    msg.setStyleSheet(ui_config.colors['centralWidget'])

    msg.exec()
