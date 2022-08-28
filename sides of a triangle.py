#finding triangle is valid or invalid using sides
a=int(input("enter length of a first side:"))
b=int(input("enter length of a second side:"))
c=int(input("enter lenth of a third side:"))
if a+b>=c and b+c>=a and c+a>=b:
    print("valid triangle")
else:
    print("invalid triangle")