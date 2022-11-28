import openpyxl as px
wb = px.load_workbook("xlsx07\sample07.xlsx")
ws = wb["注文データ"]
for row in ws.iter_rows(min_row=2, max_row=3):
    for cell in row:
        print(cell)