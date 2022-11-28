import openpyxl as px
wb = px.load_workbook('xlsx/sample06_new.xlsx')

ws_list = wb.worksheets
print(ws_list)

ws = wb.active
print(ws)

print(wb.sheetnames)
wb.close()