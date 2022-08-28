 #finding grades of a student
sub1=int(input("enter physics marks:"))
sub2=int(input("enter chemistry marks:"))
sub3=int(input("enter mathematics marks:"))
sub4=int(input("enter history marks:"))
sub5=int(input("enter political science marks:"))
sub6=int(input("enter economy marks:"))
sub7=int(input("enter computer science marks:"))
sub8=int(input("enter commerce marks:"))
total=sub1+sub2+sub3+sub4+sub5+sub6+sub7+sub8
avg=total/8
per=avg*100
if per>90:
    print("grade:A")
elif per>=80 and per<=90:
    print("grade:B")
elif per>=70 and per<=80:
    print("grade:c")
elif per>=60 and per<=70:
    print("grade:D")
elif per>=50 and per<=60:
    print("grade:E")
else:
    print("grade:F")
print(total)
print(avg)
print(per)
