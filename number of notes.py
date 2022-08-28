#number of notes for amount
amount=int(input("enter your amount:-"))
# notes=n_1000=n_500=n_200=n_100=n_50=n_20=n_10=n_5=n_2=n_1=0
if amount>=1000:
    n_1000=amount//1000
    amount=amount-n_1000*1000
    print(1000,"=",n_1000)
if amount>=500:
    n_500=amount//500
    amount=amount-n_500*500
    print(500,"=",n_500)
if amount>=200:
    n_200=amount//200
    amount=amount-n_200*200
    print(200,"=",n_200)
if amount>=100:
    n_100=amount//100
    amount=amount-n_100*100
    print(100,"=",n_100)
if amount>=50:
    n_50=amount//50
    amount=amount-n_50*50
    print(50,"=",n_50)
if amount>=20:
    n_20=amount//20
    amount=amount-n_20*20
    print(20,"=",n_20)
if amount>=10:
    n_10=amount//10
    amount=amount-n_10*10
    print(10,"=",n_10)
if amount>=5:
    n_5=amount//5
    amount=amount-n_5*5
    print(5,"=",n_5)
if amount>=2:
    n_2=amount//2
    amount=amount-n_2*2
    print(2,"=",n_2)
if amount>=1:
    n_1=amount//1
    amount=amount-n_1*1
    print(1,"=",n_1)
else:
    print("0")
