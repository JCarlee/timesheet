import datetime
import os
import shutil
import logging
from typing import List

logging.basicConfig(level=logging.INFO)


class Timesheet(object):
    """A utility class to manage and create weekly timesheets."""

    def __init__(self, root: str):
        """Initializes the Timesheet object with default values."""
        self.root = root
        self.today = datetime.datetime.now()
        self.day1 = self.today - datetime.timedelta(days=6)
        self.day1_str = f"{self.day1.month}.{self.day1.day}"
        self.day2 = self.day1 + datetime.timedelta(days=6)
        self.day2_str = f"{self.day2.month}.{self.day2.day}"
        self.year = f"{self.day1.year}"
        self.xlsx_list: List[str] = []
        self.pdf_list: List[str] = []
        self.new_xlsx = os.path.join(self.root, f"Carlee_timesheet_{self.day1_str}-{self.day2_str}_{self.year}.xlsx")

    def dir_list(self):
        """Populates the lists of .xlsx and .pdf files in the root directory."""
        for file in os.listdir(self.root):
            if file.endswith(".xlsx"):
                self.xlsx_list.append(file)
            elif file.endswith(".pdf"):
                self.pdf_list.append(file)

    def create_new(self):
        """Creates a new timesheet file."""
        if not self.xlsx_list:
            logging.error("No .xlsx files found in the directory.")
            return
        try:
            shutil.copy(os.path.join(self.root, self.xlsx_list[0]), self.new_xlsx)
            logging.info(f"Created new timesheet: {self.new_xlsx}")
        except Exception as e:
            logging.error(f"Error creating new timesheet: {e}")

    def archive(self):
        """Archives old timesheet and PDF files."""
        if not self.xlsx_list or not self.pdf_list:
            logging.error("No files to archive.")
            return
        try:
            shutil.move(os.path.join(self.root, self.xlsx_list[0]), os.path.join(self.root, "old", self.xlsx_list[0]))
            shutil.move(os.path.join(self.root, self.pdf_list[0]), os.path.join(self.root, "old", self.pdf_list[0]))
            logging.info("Archived old files.")
        except Exception as e:
            logging.error(f"Error archiving files: {e}")


def main():
    root_dir = r"G:\My Drive\Timesheets"
    timesheet = Timesheet(root_dir)
    timesheet.dir_list()
    timesheet.create_new()
    timesheet.archive()


if __name__ == "__main__":
    main()
