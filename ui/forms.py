from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QDate
from ui import config


class Label(QtWidgets.QLabel):
    def __init__(self, name, layout):
        super().__init__(config.items_text[name])
        self.setFont(config.mainfont)
        self.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        layout.addWidget(self, *config.items_coordinates[name])


class LineInput(QtWidgets.QLineEdit):
    def __init__(self, name, layout):
        super().__init__()
        self.setFont(config.mainfont)
        layout.addWidget(self, *config.items_coordinates[name])


class Spacer(QtWidgets.QSpacerItem):
    def __init__(self, name, layout):
        super().__init__(*config.items_geometry['spacers'])
        layout.addItem(self, *config.items_coordinates[name])


class DateInput(QtWidgets.QDateEdit):
    def __init__(self, name, layout):
        super().__init__()
        self.setFont(config.mainfont)
        self.setCalendarPopup(True)
        self.setDate(QDate.currentDate())
        layout.addWidget(self, *config.items_coordinates[name])


class CheckBox(QtWidgets.QCheckBox):
    def __init__(self, name, layout):
        super().__init__(config.items_text[name])
        self.setFont(config.mainfont)
        layout.addWidget(self, *config.items_coordinates[name])


class ComboBox(QtWidgets.QComboBox):
    def __init__(self, name, layout):
        super().__init__()
        self.setFont(config.mainfont)
        for i in range(config.items_text[name][0]):
            self.addItem(config.items_text[name][i + 1])
        layout.addWidget(self, *config.items_coordinates[name])


class Button(QtWidgets.QPushButton):
    def __init__(self, name, placement):
        super().__init__(config.items_text[name], placement)
        self.setGeometry(config.items_geometry[name])
        self.setFont(config.mainfont)
