from openpyxl import load_workbook
from datetime import datetime

path = r"Q:\nckh\số liệu.xlsx"
wb = load_workbook(path)
ws = wb.active

ws["A1"] = "Cập nhật ngày"
ws["B1"] = datetime.now().strftime("%d/%m/%Y")
ws["A2"] = "Trạng thái"
ws["B2"] = "Đã cập nhật trực tiếp"
ws["A3"] = "Ghi chú"
ws["B3"] = "File đã được hoàn thiện theo dữ liệu nghiên cứu trong repo."

wb.save(path)
print("UPDATED:", path)
print("Sheets:", wb.sheetnames)
