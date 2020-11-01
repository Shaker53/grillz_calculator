from dataclasses import dataclass


JAW_PRICE = 10
TOOTH_PRICE = 4
SPRAYING_PRICE = 3
COMMON_BANK_SHARE = 0.3
ANTON_SHARE = 0.35
KOSTYA_SHARE = 0.35


@dataclass
class CalculationResult:
    second_payment: float
    jaws_sum: float
    n_of_teeth_sum: float
    spraying_sum: float
    materials: float
    income: float
    common_bank: float
    anton: float
    kostya: float


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
