from ui.messages import show_msg_exelsaved, show_msg_wrong_input
from .business_logic import calculate_income_and_expenses
from ui.config import table_on_page
from ui.forms import Window
from exel import xls_export


class GrillzApp(Window):
    def __init__(self):
        super().__init__()
        self.button_calculate.clicked.connect(self.click_on_calculate_button)
        self.button_save.clicked.connect(self.click_on_save_button)

    def click_on_calculate_button(self):
        inputs = reading_inputs(self)
        result_of_check = checking_inputs(inputs)
        if result_of_check == 'wrong_input':
            show_msg_wrong_input()
            return

        inputs = prepare_inputs(inputs)
        income_and_expenses = calculate_income_and_expenses(inputs)
        self.all_params = [inputs, income_and_expenses]
        table_on_page(self.all_params, self.tableWidget)
        self.stackedWidget.setCurrentIndex(1)

    def click_on_save_button(self):
        xls_export.save_order(self.all_params)
        self.button_save.setEnabled(False)
        show_msg_exelsaved()


def reading_inputs(self):
    client_name = self.client_name.text()
    n_of_order = self.n_of_order.text()
    start_date = self.start_date.text()
    maybe_finish_date = self.maybe_finish_date.text()
    order_sum = self.order_sum.text()
    first_payment = self.first_payment.text()
    difficult_sum = self.difficult_sum.text()
    jaws = self.jaws.currentIndex()
    jaws_text = self.jaws.currentText()
    n_of_teeth = self.n_of_teeth.text()
    spraying = self.spraying.text()
    add_costs = self.add_costs.text()

    inputs = [client_name, n_of_order, start_date, maybe_finish_date, order_sum,
              first_payment, difficult_sum, jaws, jaws_text, n_of_teeth, spraying, add_costs]

    return inputs


def checking_inputs(inputs):
    for idx in [1, 4, 5, 6, 9, 10, 11]:
        if inputs[idx] != '':
            try:
                float(inputs[idx])
            except:
                return 'wrong_input'


def prepare_inputs(inputs):
    for idx in range(1, len(inputs)):
        if inputs[idx] == '':
            inputs[idx] = 0

    if inputs[7] == 0:
        inputs[7] = 1

    return inputs
