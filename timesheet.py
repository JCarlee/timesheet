import shutil
import datetime
import os


class Timesheet(object):
    def __init__(self):
        # CHANGE LINE BELOW TO YOUR DIRECTORY
        self.root = 'G:\My Drive\Timesheets\\'  # Root dir only usable on John Carlee's work desktop on Fridays
        self.today = datetime.datetime.now()    # Set 'today' to current date

        self.day1 = self.today - datetime.timedelta(days=6)               # Define first day of excel title
        self.day1_str = '{0}.{1}'.format(self.day1.month, self.day1.day)  # Create usable string for day1

        self.day2 = self.day1 + datetime.timedelta(days=6)                # Define second day of excel title
        self.day2_str = '{0}.{1}'.format(self.day2.month, self.day2.day)  # Create usable string for day2

        self.year = '{0}'.format(self.day1.year)                          # Variable to hold year string

        self.xlsx_list = []                                               # Empty list holding xlsx files in root
        self.pdf_list = []                                                # Empty list holding pdf files in root
        self.new_xlsx = \
            self.root + 'Carlee_timesheet_' + self.day1_str + '-' + self.day2_str + '_' + self.year + '.xlsx'

    def dir_list(self):
        for file in os.listdir(self.root):                                # Loop through root, make list of xlsx files
            if file.endswith(".xlsx"):
                self.xlsx_list.append(file)

        for file in os.listdir(self.root):                                # Loop through root, make list of pdf files
            if file.endswith(".pdf"):
                self.pdf_list.append(file)

    def create_new(self):
        # Make copy of previous week's timesheet with next week title
        shutil.copy(self.root + self.xlsx_list[0], self.new_xlsx)

    def archive(self):
        # Move both old files into old folder
        shutil.move(self.root + self.xlsx_list[0], self.root + 'old\\' + self.xlsx_list[0])
        shutil.move(self.root + self.pdf_list[0], self.root + 'old\\' + self.pdf_list[0])


a = Timesheet()
a.dir_list()
a.create_new()
a.archive()
