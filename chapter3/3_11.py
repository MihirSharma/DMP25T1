def check_year(year):
    mod4 = year%4
    mod100 = year%100
    mod400 = year%400

    if (mod4 == 0 and not mod100==0) or mod400 == 0:
        leap = True
    else:
        leap = False
            

    return leap

def month_size(month, year):
    month_dict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31, 13:29}
    leap = check_year(year)
    if(month == 2 and leap):
        return month_dict[13]
    else:
        return month_dict[month]

try:
    month = int(input("Enter month number (1 to 12) : "))
    year = int(input("Enter year : "))
except:
    print("Something went wrong")
    exit()

month_name = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}

day_count = month_size(month, year)

print(f"{month_name[month]} {year} has {day_count} days")
