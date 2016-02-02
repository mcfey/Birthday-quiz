"""
birthday.py
Author: Mary Feyrer
Credit: Tess Snyder
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day

name = input("Hello, what is your name? ")
birthmonth = input("Hi " + name + ", what was the name of the month you were born in? ")
birthyear = int(input("And what year were you born in, " +name+ "? "))
birthday = int(input("And the day? "))

if birthmonth == "October" and birthday == 31:
    print("You were born on Halloween!")
if birthmonth == month_name[todaymonth] and birthday == todaydate:
    print("Happy birthday!")

if birthmonth == "December" or birthmonth == "January" or birthmonth == "February":
    season = "winter"
if birthmonth == "March" or birthmonth == "April" or birthmonth == "May":
    season = "spring"
if birthmonth == "October" or birthmonth == "September" or birthmonth == "November":
    season = "fall" 
if birthmonth == "June" or birthmonth == "July" or birthmonth == "August":
    season = "summer"


if birthyear >= 1980 and birthyear <= 1989:
    decade = "eighties"
if birthyear >= 1990 and birthyear <= 1999:
    decade = "nineties"
if birthyear <= 1980:
    decade = "Stone Age"
if birthyear >= 2000:
    decade = "two thousands"

print(name + ", you are a " + season + " baby of the " + decade)



