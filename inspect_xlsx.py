import os, openpyxl
p = r'q:\nckh\số liệu.xlsx'
print('exists', os.path.exists(p), 'path', p)
wb = openpyxl.load_workbook(p, data_only=False)
print('sheets', wb.sheetnames)
for ws in wb.worksheets:
    print('---', ws.title, ws.max_row, ws.max_column)
    for row in ws.iter_rows(min_row=1, max_row=min(ws.max_row, 20), values_only=True):
        print(row)
