#finding month number and number of days in a month
monthnumber=int(input("enter your month number:"))
if monthnumber==1:
    print("january has 31 days")
elif monthnumber==2:
    print("february has 28/29 days")
elif monthnumber==3:
    print("march has 31 days")
elif monthnumber==4:
    print("april has 30 days")
elif monthnumber==5:
    print("may has 31 days")
elif monthnumber==6:
    print("june has 30 days")
elif monthnumber==7:
    print("july has 31 days")
elif monthnumber==8:
    print("august has 31 days")
elif monthnumber==9:
    print("september has 30 days")
elif monthnumber==10:
    print("october has 31 days")
elif monthnumber==11:
    print("november has 30 days")
elif monthnumber==12:
    print("december has 31 days")
else:
    print(monthnumber,"is not a month number")