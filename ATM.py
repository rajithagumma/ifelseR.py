#ATM using nested if
print("welcome to State bank of india")
print("insert your card")
print("choose your language:")
language=input("enter language:")
if language=="english":
    password=1234
    pin=int(input("enter your four digit pin:"))
    if pin==password:
        print("menu_")
        print("1_balance enquiry")
        print("2_withdrawal")
        print("3_pin generation")
        print("4_quit")  
        a=int(input("please choose your transactio"))
        m=28000
        if a==1:
            print("your available balance is",m)
            print("thanks for visiting state bank of india")
        if a==2:
            w=int(input("enter your withdrawal amount:"))
            if w<m:
                print("your amount withdrawal succesfull")
                print(m-w,"is your remaining amount")
                print("thanks for visiting state bank of india")
            else:
                print("enter valid amount")
        if a==3:
            print("OTP sent to your registered mobile number")
            OTP=input("enter your 6 digit otp:")
            if len(OTP)==6:
                otp=input("confirm your 6 digit  otp:")
                if OTP==otp:
                    pin=int(input("enter your new pin"))
                    print("your pin generation is successfull")
                    print("thanks for visiting state bank of india")
                else:
                    print("enter correct otp")
            else:
                print("enter 6 digit otp") 
        if a==4:
            print("quit")
            print("thanks for visiting state bank of india")
    else:
        print("wrong password")
else:
    print("enter valid language")