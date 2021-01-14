import openpyxl

path = "./Files/Login2 (copy).xlsx"

n = 0
wb = openpyxl.load_workbook(path)
sheets = wb.sheetnames
ws = wb[sheets[n]]