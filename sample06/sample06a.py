import openpyxl as px
wb = px.load_workbook('xlsx/sample06.xlsx')
wb.save('xlsx/sample06_new.xlsx')
wb.close()