#finding profit or loss
actualcost=int(input("enter your actual cost:"))
salecost=int(input("enter your sale cost:"))
if actualcost>salecost:
    print(actualcost-salecost,"rupees loss")
elif salecost>actualcost:
    print(salecost-actualcost,"rupees profit")
else:
    print("neither profit nor loss")