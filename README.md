# timesheet

**THIS SCRIPT IS NO LONGER USED OR UPDATED**

Utility to create weekly timesheets.


## Author
**John Carlee** - [Email me](mailto:JCarlee@gmail.com)

I am 9 year veteran in the Geographic Information Science and Cartography space.


## Motivation
I hate filling out timesheets, you hate filling out timesheets. I pulled together this script to create
the excel timesheet from the past week each Friday. No values in the xlsx are changed, because it would remove the
formatting.



## Dependencies
* Python 3
* os
* datetime
* shutil

## Getting Started
Working directory is hardcoded to "G:\My Drive\Timesheets" making this tool only functional if you change line 9.

### Scheduling

Schedule to run on the first day of every month at 9:00 AM CDT.
* Type "Task Scheduler" into windows search bar
* Open Task Scheduler
* Under **Actions** side bar, select *Create Basic Task*
* Enter a Name
* Select weekly
* Set time, start date
* Select "Start a program"
* Program/script is the python.exe path (C:\Users\JoeSmith\AppData\Local\Programs\Python\Python37-32\python.exe)
* Add arguments: C:\[YOUR_DIRECTORY]\ngs-script.py
