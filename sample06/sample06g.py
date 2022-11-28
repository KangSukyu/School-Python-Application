import openpyxl as px
wb = px.load_workbook("xlsx/sample06_new.xlsx")
ws = wb["あいさつ"]
ws.title = "朝のあいさつ"
wb.save("xlsx/sample06_new.xlsx")
wb.close()