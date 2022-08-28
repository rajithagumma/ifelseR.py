#finding middle number
a=int(input("enter first number:-"))
b=int(input("enter second number:-"))
c=int(input("enter third number:-"))
if a>b and a<c:
    print(a,"is a middle number")
elif b>a and b<c:
    print(b,"is amiddle number")
else:print(c,"is a middle number")