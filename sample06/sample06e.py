import openpyxl as px
wb = px.load_workbook("xlsx/sample06_new.xlsx")

ws1 = wb["追加シート_First"]
ws2 = wb["追加シート_Last"]
wb.remove(ws1)
wb.remove(ws2)
wb.save("xlsx/sample06_new.xlsx")
wb.close()