def calculate_income_and_expenses(inputs):
    [client_name, n_of_order, start_date, maybe_finish_date, order_sum,
     first_payment, difficult_sum, jaws, jaws_text, n_of_teeth, spraying, add_costs] = inputs

    second_payment = float(order_sum) - float(first_payment)
    jaws_sum = float(jaws * 10)
    n_of_teeth_sum = float(n_of_teeth) * 4
    spraying_sum = float(spraying) * 3
    materials = jaws_sum + n_of_teeth_sum + spraying_sum + float(add_costs)
    income = round(float(order_sum) - float(difficult_sum) - materials, 2)
    common_bank = round(income * 0.3, 2)
    anton = round(income * 0.35 + float(difficult_sum), 2)
    kostya = round(income * 0.35, 2)

    income_and_expenses = [second_payment, jaws_sum, n_of_teeth_sum, spraying_sum,
                           materials, income, common_bank, anton, kostya]

    return income_and_expenses
