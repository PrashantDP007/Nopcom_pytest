import openpyxl

def writeData(file_path ,sheet_name ,row_num ,col_num, data):
    excel_file = openpyxl.load_workbook(file_path)
    sheet = excel_file[sheet_name]

    sheet.cell(row=row_num,column=col_num).value = data
    excel_file.save(file_path)