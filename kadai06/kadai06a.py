import openpyxl as px
wb = px.Workbook()
sheet = wb.active
sheet.title = "九九"
for rowNum in range(1, 10):
	for colNum in range(1, 10):
		sheet.cell(row=rowNum, column=colNum).value = (rowNum)*(colNum)
wb.save("xlsx/9x9.xlsx")
wb.close()