#schedule
time=input("enter the timing:")
if time>="6:15am" and time<="6:59am":
    print("exercise time")
elif time>="7:00am" and time<="8:29am":
    print("freshup and breakfast time")
elif time>="8:30am" and time<="12:29pm":
    print("first coding time")
elif time>="12:30pm" and time<="13:59pm":
    print("lunch break")
elif time>="14:00pm" and time<="16:59pm":
    print("second coding time")
elif time>="17:00pm" and time<="17:59pm":
    print("break for snacks")
elif time>="18:00pm" and time<="18:59pm":
    print("english activity")
elif time>="19:00pm" and time<="19:59pm":
    print("recreation activity")
elif time>="20:00pm" and time<="20:59pm":
    print("dinner time")
else:
    print("time for rest")
