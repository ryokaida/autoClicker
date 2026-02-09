'''
Small autoclicker written in Python.
The autoclicker is set to change the location of the click based on the OS (the specific location needs to be customized to your monitor).
The autoclicker is set to go until the specified date (set in strDateBoundary).
The autoclicker is set to click on a certain minute (e.g.: the fifth minute).  This can be customized to whatever minute you want (set in strMinuteToClickOn).

Sources:
Keyboard and mouse automation in Python: https://www.geeksforgeeks.org/python/mouse-keyboard-automation-using-python/
Working with current date/time: https://www.programiz.com/python-programming/datetime/current-datetime
Using "and" in conditions in Python: https://stackoverflow.com/questions/2485466/what-is-pythons-equivalent-of-logical-and-in-an-if-statement
Using "not" in conditions in Python: https://mimo.org/glossary/python/the-not-operator
Getting the last N characters in a string: https://www.geeksforgeeks.org/python/python-get-last-n-characters-of-a-string/
Getting the OS name in Python: https://www.geeksforgeeks.org/python/get-os-name-and-version-in-python/
'''

import pyautogui
import time
from datetime import datetime
import os


# function get the current date and the last digit of the minute.  Will convert all output to String.
def getDateTime():
    # datetime object containing current date and time
    datetimeNow = datetime.now()

    # convert date into a string: dd/mm/YY H:M:S
    #  get only the date and only the minute part of the time (using string slicing)
    out_StrDate = str(datetimeNow.strftime("%m/%d/%Y"))
    out_StrLastDigitOfTime = ((str(datetimeNow.strftime("%M")))[-1:])

    return out_StrDate, out_StrLastDigitOfTime


# Main code
print(pyautogui.size())

# set the date that the autoclicker will end on
strDateBoundary = "02/14/2026"
# set the minute that the autoclicker will click on
strMinuteToClickOn = "5"

# set x and y positions based on os
if (os.name == "nt"):
    print("using windows: " + os.name)
    intX = 1000
    intY = 80
else:
    print("using linux: " + os.name)
    intX = 760
    intY = 180

pyautogui.moveTo(intX, intY, duration = 1)

# get the initial date/time
strDate, strLastDigitOfTime = getDateTime()
# initialize boolShouldClick to TRUE
boolShouldClick = True

# repeat the script until the specified date is reached
while (strDate != strDateBoundary):
    # only click on the specified minute
    if (strLastDigitOfTime == strMinuteToClickOn):
        # ensure that the click only happens once by disabling boolShouldClick
        if (boolShouldClick):
            pyautogui.moveTo(intX, intY, duration = 1)
            pyautogui.click(intX, intY)
            boolShouldClick = False
    else:
        # re-enable the click once the 5th minute has passed
        boolShouldClick = True

    # retrieve the date/time again to check it
    strDate, strLastDigitOfTime = getDateTime()