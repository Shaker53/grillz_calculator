from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QIcon
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


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui(self)

    def setup_ui(self, window):
        build_window(self, window)
        centralize(self)
        self.setWindowIcon(QIcon('images/icons/bombucha.png'))
        build_page_with_inputs(self)
        build_page_with_table(self)
        set_button_actions(self)

    def return_clicked(self):
        self.stackedWidget.setCurrentIndex(0)
        self.button_save.setEnabled(True)

    def enable_difficult(self):
        if not self.difficult_sum.isEnabled():
            self.difficult_sum.setEnabled(True)
            self.difficult_sum.setFocus()
        else:
            self.difficult_sum.clear()
            self.difficult_sum.setEnabled(False)


def set_button_actions(ui):
    ui.check_difficult.clicked.connect(ui.enable_difficult)
    ui.button_return.clicked.connect(ui.return_clicked)


def centralize(ui):
    placement = ui.frameGeometry()
    screen_center = QtWidgets.QDesktopWidget().availableGeometry().center()
    placement.moveCenter(screen_center)
    ui.move(placement.topLeft())


def build_window(ui, window):
    ui.window = window
    ui.window.setWindowTitle(config.window_title)
    ui.window.setMinimumSize(config.items_geometry['window'])
    ui.window.setMaximumSize(config.items_geometry['window'])
    build_centralWidget(ui)


def build_centralWidget(ui):
    ui.centralWidget = QtWidgets.QWidget(ui.window)
    ui.centralWidget.setMinimumSize(config.items_geometry['window'])
    ui.centralWidget.setMaximumSize(config.items_geometry['window'])
    ui.centralWidget.setStyleSheet(config.colors['centralWidget'])
    ui.window.setCentralWidget(ui.centralWidget)
    build_stackedWidget(ui)


def build_stackedWidget(ui):
    ui.stackedWidget = QtWidgets.QStackedWidget(ui.centralWidget)
    ui.stackedWidget.setGeometry(config.items_geometry['stackedWidget'])


def build_page_with_inputs(ui):
    ui.page1 = QtWidgets.QWidget()
    ui.stackedWidget.addWidget(ui.page1)
    ui.layoutWidget = QtWidgets.QWidget(ui.page1)
    ui.layoutWidget.setGeometry(config.items_geometry['layoutWidget'])
    ui.gridLayout = QtWidgets.QGridLayout(ui.layoutWidget)

    ui.spacer1 = Spacer('spacer1', ui.gridLayout)
    ui.spacer2 = Spacer('spacer2', ui.gridLayout)
    ui.spacer3 = Spacer('spacer3', ui.gridLayout)
    ui.spacer4 = Spacer('spacer4', ui.gridLayout)
    ui.spacer5 = Spacer('spacer5', ui.gridLayout)

    ui.button_calculate = Button('button_calculate', placement=ui.page1)
    ui.gridLayout.addWidget(ui.button_calculate, *config.items_coordinates['button_calculate'])

    build_all_input_fields(ui)


def build_all_input_fields(ui):
    ui.label_n_of_order = Label('label_n_of_order', ui.gridLayout)
    ui.label_client_name = Label('label_client_name', ui.gridLayout)
    ui.label_start_date = Label('label_start_date', ui.gridLayout)
    ui.label_maybe_finish_date = Label('label_maybe_finish_date', ui.gridLayout)
    ui.label_order_sum = Label('label_order_sum', ui.gridLayout)
    ui.label_first_payment = Label('label_first_payment', ui.gridLayout)
    ui.label_jaws = Label('label_jaws', ui.gridLayout)
    ui.label_n_of_teeth = Label('label_n_of_teeth', ui.gridLayout)
    ui.label_spraying = Label('label_spraying', ui.gridLayout)
    ui.label_add_costs = Label('label_add_costs', ui.gridLayout)

    ui.n_of_order = LineInput('input_n_of_order', ui.gridLayout)
    ui.client_name = LineInput('input_client_name', ui.gridLayout)
    ui.order_sum = LineInput('input_order_sum', ui.gridLayout)
    ui.first_payment = LineInput('input_first_payment', ui.gridLayout)
    ui.difficult_sum = LineInput('input_difficult_sum', ui.gridLayout)
    ui.n_of_teeth = LineInput('input_n_of_teeth', ui.gridLayout)
    ui.spraying = LineInput('input_spraying', ui.gridLayout)
    ui.add_costs = LineInput('input_add_costs', ui.gridLayout)
    ui.difficult_sum.setEnabled(False)

    ui.maybe_finish_date = DateInput('input_maybe_finish_date', ui.gridLayout)
    ui.start_date = DateInput('input_start_date', ui.gridLayout)
    ui.check_difficult = CheckBox('check_difficult', ui.gridLayout)
    ui.jaws = ComboBox('input_jaws', ui.gridLayout)


def build_page_with_table(ui):
    ui.page2 = QtWidgets.QWidget()
    ui.page2.setMinimumSize(config.items_geometry['page_2'])
    ui.stackedWidget.addWidget(ui.page2)

    ui.button_return = Button('button_return', placement=ui.page2)
    ui.button_save = Button('button_save', placement=ui.page2)
    build_table_frame(ui)


def build_table_frame(ui):
    ui.tableWidget = QtWidgets.QTableWidget(ui.page2)
    ui.tableWidget.setGeometry(config.items_geometry['tableWidget'])
    ui.tableWidget.setRowCount(config.table_rows)
    ui.tableWidget.setColumnCount(config.table_columns)

    ui.tableWidget.horizontalHeader().setVisible(False)
    ui.tableWidget.horizontalHeader().setDefaultSectionSize(config.items_geometry['table_items_width'])
    ui.tableWidget.verticalHeader().setVisible(False)
    ui.tableWidget.verticalHeader().setDefaultSectionSize(config.items_geometry['table_items_height'])
