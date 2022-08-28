#finding valid or invalid triangle
a=int(input("enter first angle of a triangle:"))
b=int(input("entersecond angle of  a triangle:"))
c=int(input("enter third angle of a triangle:"))
total=a+b+c
if total==180:
    print("valid triangle")
else:
    print("invalid trianle")