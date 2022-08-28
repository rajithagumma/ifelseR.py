month=input("enter the month:")
date=int(input("enter the date:"))
day=input("enter the day:")
if month in ("nov" "dec" "jan" "feb"):
    if date>=1 and date<=31:
        if day in ("sun" "mon" "tue" "wed" "thu" "fri" "sat"):
            print("winter season")
        else:
            print("not a winter season")
    else:
        print("not winter")
else:
    print("not winter")
if month in ("march" "april" "may" "june"):
    if date>=1 and date<=31:
        if day in ("sun" "mon" "tue" "wed" "thu" "fri" "sat"):
            print("summer season")
        else:
            print("not summer")
    else:
        print("not summer")
else:
    print("not summer")
if month in("july" "sep" "oct"):
    if date>=1 and date<=31:
        if day in ("sun""mon" "tue" "wed" "thu" "fri" "sat"):
            print("rainy season")
        else:
            print("not rainy")
    else:
        print("not rainy")
else:
    print("not rainy")