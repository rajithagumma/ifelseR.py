#finding equilateral  or isoceles or scalene triangle
a=int(input("enter length of a first side:"))
b=int(input("enter lenth of a second side:"))
c=int(input("enter length of a third side"))
if a==b==c:
    print("equilateral triangle")
elif a==b or b==c or c==a:
    print("isoceles triangle")
else:
    print("scalene triangle")