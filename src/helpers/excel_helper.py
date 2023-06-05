from openpyxl import load_workbook


def read_workbook(file):
    print(__file__, file)
    return load_workbook(file, data_only=True)


def get_defined_name_cell_value(wb, name):
    if '+' in wb.defined_names[name].value:
        cells = wb.defined_names[name].value.split('+')
        value = 0.0

        for cell in cells:
            title, coord = cell.split('!')
            value += wb[title][coord].value

        return value
    else:
        destination = wb.defined_names[name].destinations

        for title, coord in destination:
            return wb[title][coord].value
