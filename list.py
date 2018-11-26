# import os
# from  openpyxl import Workbook
# import datetime
# system = os.name
# env = os.environ
# filePath = os.path.abspath('.')
# print(system)
# print(filePath)
# 
# wb = Workbook()
# ws = wb.active
# ws.title = "platform"
# ws['A1'] = 42
# ws.append([1,2,3])
# ws['b1'] = datetime.datetime.now()
# ws['A3'] = system
# ws['A4'] = filePath
# ws1 = wb.create_sheet("win2019")
# ws2 = wb.create_sheet("win2016")
# ws3 = wb.create_sheet("rhel7")
# ws4 = wb.create_sheet("suse12")
#
# wb.save("sample.xlsx")
