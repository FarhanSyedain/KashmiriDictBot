from functions import replace
from openpyxl import *
import CONST


wb = load_workbook(CONST.WB_PATH)
sheet = wb['Main']
for i in range(2,sheet.max_row):
	cell_value = sheet[f'F{i}'].value
	new_value = replace(cell_value)
	sheet[f'F{i}'].value = new_value

wb.save('Generated/generatedWB.xlsx')


