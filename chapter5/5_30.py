# Input year and first day of the year
year = int(input("Enter the year (e.g., 2013): "))
first_day = int(input("Enter the first day of the year (0=Sunday, 1=Monday, ..., 6=Saturday): "))

# Determine if it's a leap year
leap = False
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    leap = True

# Set current day counter to the first day
current_day = first_day
month = 1

while month <= 12:
    # Get month name and number of days
    if month == 1:
        month_name = "January"
        days = 31
    elif month == 2:
        month_name = "February"
        if leap:
            days = 29
        else:
            days = 28
    elif month == 3:
        month_name = "March"
        days = 31
    elif month == 4:
        month_name = "April"
        days = 30
    elif month == 5:
        month_name = "May"
        days = 31
    elif month == 6:
        month_name = "June"
        days = 30
    elif month == 7:
        month_name = "July"
        days = 31
    elif month == 8:
        month_name = "August"
        days = 31
    elif month == 9:
        month_name = "September"
        days = 30
    elif month == 10:
        month_name = "October"
        days = 31
    elif month == 11:
        month_name = "November"
        days = 30
    elif month == 12:
        month_name = "December"
        days = 31

    # Get day name
    if current_day == 0:
        day_name = "Sunday"
    elif current_day == 1:
        day_name = "Monday"
    elif current_day == 2:
        day_name = "Tuesday"
    elif current_day == 3:
        day_name = "Wednesday"
    elif current_day == 4:
        day_name = "Thursday"
    elif current_day == 5:
        day_name = "Friday"
    elif current_day == 6:
        day_name = "Saturday"

    # Print result
    print(month_name,"1,",year, " is ", day_name)

    # Update current_day for next month
    current_day = (current_day + days) % 7
    month += 1