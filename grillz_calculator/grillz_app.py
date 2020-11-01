from grillz_calculator.ui import messages
from .money_flow_calculator import calculate_income_and_expenses
from config import ui_config
from grillz_calculator.ui import forms
from grillz_calculator.exel import xls_export
from dataclasses import dataclass


@dataclass
class ClientParams:
    client_name: str
    n_of_order: str
    start_date: str
    maybe_finish_date: str


@dataclass
class MoneyParams:
    order_sum: str
    first_payment: str
    difficult_sum: str
    jaws: int
    jaws_text: str
    n_of_teeth: str
    spraying: str
    add_costs: str


class GrillzApp(forms.Window):
    def __init__(self):
        super().__init__()
        self.button_calculate.clicked.connect(self.click_on_calculate_button)
        self.button_save.clicked.connect(self.click_on_save_button)
        self.all_params = {}

    def click_on_calculate_button(self):
        client_params, money_params = reading_inputs(self)
        validated = validate_inputs(money_params)

        if not validated:
            messages.show_msg_wrong_input()
            return

        got_all_important_params = check_got_all_important_params(client_params, money_params)
        if not got_all_important_params:
            back_button_pushed = messages.show_msg_not_all_important_params()
            if back_button_pushed:
                return

        prepared = prepare_to_calculate(money_params)
        money_params_prepared = MoneyParams(*prepared)
        calculation_result = calculate_income_and_expenses(money_params_prepared)
        self.all_params = {
            'client_params': client_params,
            'money_params_prepared': money_params_prepared,
            'calculation_result': calculation_result
        }
        ui_config.table_on_page(self.all_params, self.tableWidget)
        self.stackedWidget.setCurrentIndex(1)

    def click_on_save_button(self):
        xls_export.save_order(self.all_params)
        self.button_save.setEnabled(False)
        messages.show_msg_exelsaved()


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

    client_params = ClientParams(
        client_name, n_of_order, start_date, maybe_finish_date
    )
    money_params = MoneyParams(
        order_sum, first_payment, difficult_sum,
        jaws, jaws_text, n_of_teeth, spraying, add_costs
    )

    return client_params, money_params


def validate_inputs(money_params):
    only_numeral_inputs = [
        money_params.order_sum, money_params.first_payment, money_params.difficult_sum,
        money_params.n_of_teeth, money_params.spraying, money_params.add_costs
    ]
    for parameter in only_numeral_inputs:
        if parameter != '':
            try:
                float(parameter.replace(',', '.'))
            except ValueError:
                return False
        return True


def check_got_all_important_params(client_params, money_params):
    important_params = [
        client_params.client_name, client_params.n_of_order,
        money_params.order_sum, money_params.n_of_teeth
    ]
    if any(parameter == '' for parameter in important_params):
        return False
    else:
        return True


def prepare_to_calculate(money_params):
    money_params.jaws = 1 if money_params.jaws == 0 else money_params.jaws

    to_prepare = [
        money_params.order_sum, money_params.first_payment,
        money_params.difficult_sum, money_params.jaws, money_params.jaws_text,
        money_params.n_of_teeth, money_params.spraying, money_params.add_costs
    ]
    prepared = []

    for parameter in to_prepare:
        if parameter == '':
            prepared.append(0)
        else:
            parameter = parameter.replace(',', '.') if isinstance(parameter, str) else parameter
            prepared.append(parameter)

    return prepared
