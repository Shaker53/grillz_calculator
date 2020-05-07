from xlrd import open_workbook
from xlwt import Workbook
from exel import config


def save_order(all_params):
    [client_name, n_of_order, start_date, maybe_finish_date, order_sum, first_payment, difficult_sum,
     jaws, jaws_text, n_of_teeth, spraying, add_costs], [second_payment, jaws_sum, n_of_teeth_sum, spraying_sum,
     materials, income, common_bank, anton, kostya] = all_params

    for_export = [
        int(n_of_order), client_name, start_date, maybe_finish_date, float(order_sum), float(difficult_sum),
        float(add_costs), income, common_bank, anton, kostya, float(first_payment), second_payment, materials,
        jaws_text, jaws_sum, float(n_of_teeth), n_of_teeth_sum, float(spraying), spraying_sum
    ]

    try:
        file = open_workbook('zakazy.xls', formatting_info=True)
    except FileNotFoundError:
        wb = Workbook()
        worksheet = wb.add_sheet('zakazy')
        i = 0
        for label in config.table_labels:
            worksheet.write(0, i, label)
            i += 1
        wb.save('zakazy.xls')
        file = open_workbook('zakazy.xls', formatting_info=True)
    sheet = file.sheet_by_index(0)
    table = []
    for m in range(len(sheet.col(0))):
        my_row = []
        for n in range(len(sheet.row(m))):
            my_row.append(sheet.row(m)[n].value)
        table.append(my_row)
    table.append(for_export)
    wb = Workbook()
    worksheet = wb.add_sheet('zakazy')
    j = 0
    for row in table:
        k = 0
        for element in row:
            worksheet.write(j, k, element)
            k += 1
        j += 1

    for i in config.numbers_of_wide_cols:
        worksheet.col(i).width = 256 * 20
    wb.save('zakazy.xls')
