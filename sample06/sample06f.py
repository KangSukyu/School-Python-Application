import openpyxl as px
wb = px.load_workbook("xlsx/sample06_new.xlsx")

ws = wb["あいさつ"]
wb.copy_worksheet(ws)
wb.save("xlsx/sample06_new.xlsx")
wb.close()