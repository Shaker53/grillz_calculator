from PyQt5.QtCore import QCoreApplication, QSize, QRect, Qt
from PyQt5.QtGui import QColor, QFont, QBrush
from PyQt5.QtWidgets import QTableWidgetItem


class Font(QFont):
    def __init__(self, size=12):
        super().__init__()
        self.setFamily('Arial')
        self.setPointSize(size)
        self.setBold(False)
        self.setWeight(75)
        self.setStyleStrategy(QFont.PreferDefault)


bigfont = Font(14)
mainfont = Font()
littlefont = Font(11)

window_title = QCoreApplication.translate('window', 'GRILLZ TURBOCALCULATOR')

table_rows = 10
table_columns = 5

items_text = {
    'label_n_of_order': ' Номер заказа* ',
    'label_client_name': ' Имя заказчика*  ',
    'label_start_date': 'Дата заказа',
    'label_maybe_finish_date': 'Дата окончания ',
    'label_order_sum': ' Общ. сумма заказа* ',
    'label_first_payment': ' Первый взнос  ',
    'label_jaws': 'Челюсти  ',
    'label_n_of_teeth': ' Количество  зубов* ',
    'label_spraying': 'Напыление ',
    'label_add_costs': 'Доп.расходы',
    'check_difficult': 'Cложная работа,\nдополнительные\nукрашения и т.д.',
    'input_jaws': [3, 'нижняя', 'верхняя', 'нижн. и верх.'],
    'button_calculate': 'Рассчитать',
    'button_return': 'Назад',
    'button_save': 'Сохранить заказ',
    'msg_exelsaved_window_title': 'Пора за работу',
    'msg_exelsaved_text': '   Заказ успешно сохранен!   ',
    'msg_not_all_important_params_window_title': 'Внимание!',
    'msg_not_all_important_params_text': 'Вы заполнили не все обязательные поля\n',
    'msg_not_all_important_params_button_ok': '  Сейчас заполню  ',
    'msg_not_all_important_params_button_no': '  Плевать  ',
    'msg_wrong_input_window_title': 'Внимание!',
    'msg_wrong_input_text': 'Вы неправильно заполнили поля ввода\n',


}

items_coordinates = {
    'label_n_of_order': [0, 1, 1, 1],
    'label_client_name': [2, 1, 1, 1],
    'label_start_date': [4, 1, 1, 1],
    'label_maybe_finish_date': [6, 1, 1, 1],
    'label_order_sum': [0, 3, 1, 1],
    'label_first_payment': [2, 3, 1, 1],
    'label_jaws': [0, 5, 1, 1],
    'label_n_of_teeth': [2, 5, 1, 1],
    'label_spraying': [4, 5, 1, 1],
    'label_add_costs': [6, 5, 1, 1],

    'input_n_of_order': [1, 1, 1, 1],
    'input_client_name': [3, 1, 1, 1],
    'input_order_sum': [1, 3, 1, 1],
    'input_first_payment': [3, 3, 1, 1],
    'input_difficult_sum': [7, 3, 1, 1],
    'input_n_of_teeth': [3, 5, 1, 1],
    'input_spraying': [5, 5, 1, 1],
    'input_add_costs': [7, 5, 1, 1],

    'spacer1': [4, 2, 1, 1],
    'spacer2': [4, 0, 1, 1],
    'spacer3': [8, 3, 1, 1],
    'spacer4': [4, 6, 1, 1],
    'spacer5': [4, 4, 1, 1],

    'input_maybe_finish_date': [7, 1, 1, 1],
    'input_start_date': [5, 1, 1, 1],

    'check_difficult': [4, 3, 3, 1],
    'input_jaws': [1, 5, 1, 1],
    'button_calculate': [9, 3, 1, 1]
}

items_geometry = {
    'window': QSize(824, 478),
    'stackedWidget': QRect(0, -16, 811, 480),
    'layoutWidget': QRect(0, 20, 825, 426),
    'page_2': QSize(811, 480),
    'tableWidget': QRect(5, 25, 804, 394),

    'table_items_height': 39,
    'table_items_width': 160,

    'button_return': QRect(180, 434, 203, 40),
    'button_save': QRect(430, 434, 203, 40),
    'button_calculate': QRect(430, 434, 218, 40),
    'spacers': [40, 20]
}

colors = {
    'centralWidget': 'color: rgb(31, 85, 94)',
    'table_separators': QColor(193, 193, 193),
    'table_main_items': QColor(205, 245, 255)
}


def table_on_page(all_params, tableWidget):
    [client_name, n_of_order, start_date, maybe_finish_date, order_sum, first_payment, difficult_sum,
     jaws, jaws_text, n_of_teeth, spraying, add_costs], [second_payment, jaws_sum, n_of_teeth_sum, spraying_sum,
     materials, income, common_bank, anton, kostya] = all_params
    table_information = {
        (0, 0): ['---------', ' № заказа'],
        (0, 1): ['---------', n_of_order],
        (0, 2): ['separator', ''],
        (0, 3): ['main_item',  ' Доход'],
        (0, 4): ['main_item', str(income) + ' р.'],
        (1, 0): ['main_item', ' Имя клиента'],
        (1, 1): ['main_item', client_name],
        (1, 2): ['separator', ''],
        (1, 3): ['---------', ' Общ.банк'],
        (1, 4): ['---------', str(common_bank) + ' р.'],
        (2, 0): ['---------', ' Дата заказа'],
        (2, 1): ['---------', start_date],
        (2, 2): ['separator', ''],
        (2, 3): ['---------', ' Антон'],
        (2, 4): ['---------', str(anton) + ' р.'],
        (3, 0): ['---------', ' Выполнить к'],
        (3, 1): ['---------', maybe_finish_date],
        (3, 2): ['separator', ''],
        (3, 3): ['---------', ' Костя'],
        (3, 4): ['---------', str(kostya) + ' р.'],
        (4, 0): ['separator', ''],
        (4, 1): ['separator', ''],
        (4, 2): ['separator', ''],
        (4, 3): ['---------', ' 1й взнос'],
        (4, 4): ['---------', str(float(first_payment)) + ' р.'],
        (5, 0): ['main_item', ' Общая сумма'],
        (5, 1): ['main_item', str(order_sum) + ' р.'],
        (5, 2): ['separator', ''],
        (5, 3): ['---------', ' 2й взнос'],
        (5, 4): ['---------', str(second_payment) + ' р.'],
        (6, 0): ['separator', ''],
        (6, 1): ['separator', ''],
        (6, 2): ['separator', ''],
        (6, 3): ['main_item', ' Материалы'],
        (6, 4): ['main_item', str(materials) + ' р.'],
        (7, 0): ['---------', ' Сложность'],
        (7, 1): ['---------', str(difficult_sum) + ' р.'],
        (7, 2): ['separator', ''],
        (7, 3): ['---------',' Челюсти'],
        (7, 4): ['---------', str(jaws_sum) + ' р.'],
        (8, 0): ['separator', ''],
        (8, 1): ['separator', ''],
        (8, 2): ['separator', ''],
        (8, 3): ['---------', ' Зубы'],
        (8, 4): ['---------', str(n_of_teeth_sum) + ' р.'],
        (9, 0): ['---------', ' Доп.расходы'],
        (9, 1): ['---------', str(add_costs) + ' р.'],
        (9, 2): ['separator', ''],
        (9, 3): ['---------', ' Напыление'],
        (9, 4): ['---------', str(spraying_sum) + ' р.']
    }
    for i in range(10):
        for j in range(5):
            item = QTableWidgetItem(table_information[(i, j)][1])
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            item.setFont(mainfont)
            type_ = table_information[(i, j)][0]
            if type_ == 'separator':
                brush = QBrush(colors['table_separators'])
                brush.setStyle(Qt.Dense5Pattern)
                item.setBackground(brush)
            elif type_ == 'main_item':
                brush = QBrush(colors['table_main_items'])
                brush.setStyle(Qt.Dense5Pattern)
                item.setBackground(brush)
            tableWidget.setItem(i, j, item)
