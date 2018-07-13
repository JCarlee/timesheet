import shutil
import datetime
import os

root = 'G:\My Drive\Timesheets\\'  # Root dir only usable on John Carlee's work desktop
today = datetime.datetime.now()    # Set today to current date

day1 = today - datetime.timedelta(days=6)          # Define first day of excel title
day1_str = '{0}.{1}'.format(day1.month, day1.day)  # Create usable string for day1

day2 = day1 + datetime.timedelta(days=6)           # Define second day of excel title
day2_str = '{0}.{1}'.format(day2.month, day2.day)  # Create usable string for day2

year = '{0}'.format(day1.year)                     # Variable to hold year string

xlsx_list = []                                     # Empty list holding xlsx files in root
pdf_list = []                                      # Empty list holding pdf files in root

for file in os.listdir(root):                      # Loop through root, make list of xlsx files
    if file.endswith(".xlsx"):
        xlsx_list.append(file)

for file in os.listdir(root):                      # Loop through root, make list of pdf files
    if file.endswith(".pdf"):
        pdf_list.append(file)

# define new xlsx path
new_xlsx = root + 'Carlee_timesheet_' + day1_str + '-' + day2_str + '_' + year + '.xlsx'

shutil.copy(root + xlsx_list[0], new_xlsx)         # Make copy of previous week's timesheet with next week title

# Move both old files into old folder
shutil.move(root + xlsx_list[0], root + 'old\\' + xlsx_list[0])
shutil.move(root + pdf_list[0], root + 'old\\' + pdf_list[0])
