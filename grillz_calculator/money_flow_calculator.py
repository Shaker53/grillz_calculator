JAW_PRICE = 10
TOOTH_PRICE = 4
SPRAYING_PRICE = 3
COMMON_BANK_SHARE = 0.3
ANTON_SHARE = 0.35
KOSTYA_SHARE = 0.35


class CalculationResult:
    def __init__(
            self, second_payment, jaws_sum, n_of_teeth_sum, spraying_sum,
            materials, income, common_bank, anton, kostya
    ):

        self.second_payment = second_payment
        self.jaws_sum = jaws_sum
        self.n_of_teeth_sum = n_of_teeth_sum
        self.spraying_sum = spraying_sum
        self.materials = materials
        self.income = income
        self.common_bank = common_bank
        self.anton = anton
        self.kostya = kostya


def calculate_income_and_expenses(money_params_prepared):

    second_payment = float(money_params_prepared.order_sum) - float(money_params_prepared.first_payment)
    jaws_sum = float(money_params_prepared.jaws * JAW_PRICE)
    n_of_teeth_sum = float(money_params_prepared.n_of_teeth) * TOOTH_PRICE
    spraying_sum = float(money_params_prepared.spraying) * SPRAYING_PRICE
    materials = jaws_sum + n_of_teeth_sum + spraying_sum + float(money_params_prepared.add_costs)
    income = round(float(money_params_prepared.order_sum) - float(money_params_prepared.difficult_sum) - materials, 2)
    common_bank = round(income * COMMON_BANK_SHARE, 2)
    anton = round(income * ANTON_SHARE + float(money_params_prepared.difficult_sum), 2)
    kostya = round(income * KOSTYA_SHARE, 2)
    calculation_result = CalculationResult(
        second_payment, jaws_sum, n_of_teeth_sum, spraying_sum,
        materials, income, common_bank, anton, kostya
    )

    return calculation_result
