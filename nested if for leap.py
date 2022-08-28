#finding leap year using nested if
year=int(input("enter your year:"))
if year%4==0:
    if year%400==0:
            print(year,"is a leap year")
    else:
        print(year,"is not a leap year")
else:
    print(year,"is not a leap year")