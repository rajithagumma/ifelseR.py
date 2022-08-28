#finding alpha or digit or special character
ch=input("enter your character:")
if (ch>="a" and ch<="z") and (ch>="A" and ch<="Z"):
    print(ch,"is a alphabet")
elif ch>="1"and ch<="9":
    print(ch,"is an digit")
else:
    print(ch,"is a special character")