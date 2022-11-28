import openpyxl as px
wb = px.load_workbook("xlsx\diary.xlsx")
ws = wb.active

text = input("登録するテキストを入力ーー＞")
ws["A3"] = text

wb.save("xlsx/diary.xlsx")
wb.close()