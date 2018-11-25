from openpyxl import Workbook
from openpyxl import load_workbook
import sys

wb = load_workbook('./sample.xlsx')
print(wb.sheetnames)
