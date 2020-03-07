from openpyxl import load_workbook

wb = load_workbook('template.xlsx')

# grab the active worksheet
ws = wb.active

# Data can be assigned directly to cells
ws['C20'] = 'Ciao'
ws['C22'] = 'pippo'

# Save the file
wb.save('prova.xlsx')