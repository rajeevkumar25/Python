import openpyxl

filepath="C:\Rajeev\Projects\Python\Practice\Python"
print(filepath)

def readexcel(fpath):
	wbook=openpyxl.load_workbook('test.xlsx')
	ws1=wbook.create_sheet
	ws1.title
	print(wbook.active())

  	# sheename= wbook.get_sheet_names()
  	# #print(sheename)

  	# sheet=wbook.get_sheet_by_name('Sheet1')
  	# print(sheet)
  	# print(sheet['A1'].value)
  	# print(sheet.title)

  	# anotherSheet=wbook.active
  	# print(anotherSheet)

readexcel(filepath)

