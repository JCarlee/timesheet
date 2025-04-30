# Timesheet Utility

**This project does not receive updates.**

Utility to create weekly timesheets.
## Overview

This utility generates a new Excel timesheet for the current week based on the previous week's file. It also archives old timesheets and associated PDF files into a designated folder.

---

## Features

- Automatically creates a new timesheet for the current week.
- Archives old timesheets and PDF files.
- Simple and lightweight script.

---

## Requirements

- **Python 3**
- Modules: `os`, `datetime`, `shutil`, `logging`

---

## Setup

### 1. Update the Root Directory
The working directory is hardcoded to `G:\My Drive\Timesheets`. Update this path in the script (`line 9`) to match your desired directory.

### 2. Install Dependencies
Ensure Python 3 is installed. The required modules (`os`, `datetime`, `shutil`, `logging`) are part of the Python standard library, so no additional installation is needed.

---

## Usage

### Running the Script
1. Open a terminal or command prompt.
2. Run the script using:
   ```bash
   python timesheet.pySchedule to run on the first day of every month at 9:00 AM CDT.
* Type "Task Scheduler" into windows search bar
* Open Task Scheduler
* Under **Actions** side bar, select *Create Basic Task*
* Enter a Name
* Select weekly
* Set time, start date
* Select "Start a program"
* Program/script is the python.exe path (C:\Users\JoeSmith\AppData\Local\Programs\Python\Python37-32\python.exe)
* Add arguments: C:\[YOUR_DIRECTORY]\ngs-script.py
