#finding vowel or consonent
a=input("enter your character:")
if a in ("a" "e" "i" "o" "u"):
    print(a,"is a vowel")
elif (a>="a" and a<="z") or (a>="A" and a<="Z"):
    print(a,"is a constant") 
else:
    print(a,"no alphabet or vowel")