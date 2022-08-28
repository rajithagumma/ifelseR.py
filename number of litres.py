L=int(input("enter number of litres:-"))
if L<15:
    print(15-L,"litres need to be filled")
elif L>15:
    print(15-L,"litres overflow")
elif L==15:
    print("no need to fill water")