#room shifting
girls=int(input("enter number of girls in a room:"))
beds=int(input("enter number of beds in a room:"))
if girls>beds:
    print(girls-beds,"girls shift to another room")
elif beds>girls:
    print(beds-girls,"beds left in this room")
elif girls==beds:
    print("sufficient no one want to shift")
else:
    print("not sufficient")