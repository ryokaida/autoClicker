# autoClicker
Small autoclicker written in Python.

# Prerequisites
- Python must be installed on your machine
- pip must be installed on your machine
- pyautogui must be installed on your machine
  - If it is not you may need to install it using pip: `pip install pyautogui`

# Instructions for Editing the File
- The autoclicker is set to change the location of the click based on the OS (the specific location needs to be customized to your monitor).
- The autoclicker is set to go until the specified date (set in strDateBoundary).
- The autoclicker is set to click on a certain minute (e.g.: the fifth minute).  This can be customized to whatever minute you want (set in strMinuteToClickOn).

# Instrucitons for Running the File
1. After cloning the repo, navigate to the location where you stored the **autoclicker.py file** in your terminal/Command Prompt/PowerShell
2. Use the command `python autoclicker.py`
    - You may need to allow the computer to use Remote Control (this ocurred for me on Linux)

# Sources
- Keyboard and mouse automation in Python: https://www.geeksforgeeks.org/python/mouse-keyboard-automation-using-python/
- Working with current date/time: https://www.programiz.com/python-programming/datetime/current-datetime
- Using "and" in conditions in Python: https://stackoverflow.com/questions/2485466/what-is-pythons-equivalent-of-logical-and-in-an-if-statement
- Using "not" in conditions in Python: https://mimo.org/glossary/python/the-not-operator
- Getting the last N characters in a string: https://www.geeksforgeeks.org/python/python-get-last-n-characters-of-a-string/
- Getting the OS name in Python: https://www.geeksforgeeks.org/python/get-os-name-and-version-in-python/
