from turtle import title
import openpyxl as px
wb = px.load_workbook("xlsx/sample06_new.xlsx")

for ws in wb.worksheets:
    title = ws.title
    if title == "消される運命のシート":
        wb.remove(ws)
wb.save("xlsx/sample06_new.xlsx")
wb.close()