 #finding middle number using nested if
a=int(input("enter first number:-"))
b=int(input("enter second number:-"))
c=int(input("enter second number:-"))
if a>b:
    if a<c:
        print(a,"is a middle number")
if b>a:
    if b<c:
        print(b,"is a middle number")
if c>a:
    if c<b:
        print(c,"is a middle number")
else:
    print("not a middle number")
