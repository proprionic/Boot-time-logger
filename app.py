import psutil
import datetime
from openpyxl import Workbook, load_workbook
import os

def boot_time():
    boot = 0
    boot += 1
    current_time = datetime.datetime.now()  # Get current time directly

    # -- Save to txt --
    with open("boot_logs.txt", "a") as file:
        file.write(f"Boot time: {current_time}\n")

    # -- Save to Excel --
    filename = "boot_logs.xlsx"

    # Check if the file exists
    if os.path.exists(filename):
        workbook = load_workbook(filename)  # Load existing Excel file
        sheet = workbook.active
    else:
        workbook = Workbook()  # Create new file
        sheet = workbook.active
        sheet["A1"] = "Boot Times"  # Add header row if new

    # Append boot time to next empty row
    next_row = sheet.max_row + 1
    sheet[f"A{next_row}"] = str(current_time)

    workbook.save(filename)
    print(f"✅ Boot logged at: {current_time}")

print("Logging boot time")
boot_time()
print("Boot time logged.")
