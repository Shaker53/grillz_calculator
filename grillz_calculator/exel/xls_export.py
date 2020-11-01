from xlrd import open_workbook
from xlwt import Workbook
from config import exel_config


def save_order(all_params):
    client_params = all_params['client_params']
    money_params_prepared = all_params['money_params_prepared']
    calculation_result = all_params['calculation_result']

    new_table_row = [
        client_params.n_of_order, client_params.client_name, client_params.start_date,
        client_params.maybe_finish_date, float(money_params_prepared.order_sum),
        float(money_params_prepared.difficult_sum), float(money_params_prepared.add_costs),
        calculation_result.income, calculation_result.common_bank, calculation_result.anton,
        calculation_result.kostya, float(money_params_prepared.first_payment),
        calculation_result.second_payment, calculation_result.materials, money_params_prepared.jaws_text,
        calculation_result.jaws_sum, float(money_params_prepared.n_of_teeth), calculation_result.n_of_teeth_sum,
        float(money_params_prepared.spraying), calculation_result.spraying_sum
    ]

    file = open_file_or_create_it()
    sheet = file.sheet_by_index(0)

    table = cache_document_for_modification(sheet)
    table.append(new_table_row)
    workbook, worksheet = build_modificated_file(table)

    for number_of_wide_col in exel_config.numbers_of_wide_cols:
        worksheet.col(number_of_wide_col).width = 256 * 20
    workbook.save('zakazy.xls')


def open_file_or_create_it():
    try:
        file = open_workbook('zakazy.xls', formatting_info=True)
    except FileNotFoundError:
        workbook = Workbook()
        worksheet = workbook.add_sheet('zakazy')
        col_number = 0
        for label in exel_config.table_labels:
            worksheet.write(0, col_number, label)
            col_number += 1
        workbook.save('zakazy.xls')
        file = open_workbook('zakazy.xls', formatting_info=True)
    return file


def cache_document_for_modification(sheet):
    table = []
    for col_number_ in range(len(sheet.col(0))):
        my_row = []
        for row_number_ in range(len(sheet.row(col_number_))):
            my_row.append(sheet.row(col_number_)[row_number_].value)
        table.append(my_row)
    return table


def build_modificated_file(table):
    workbook = Workbook()
    worksheet = workbook.add_sheet('zakazy')
    row_number__ = 0
    for row in table:
        col_number__ = 0
        for element in row:
            worksheet.write(row_number__, col_number__, element)
            col_number__ += 1
        row_number__ += 1
    return workbook, worksheet
