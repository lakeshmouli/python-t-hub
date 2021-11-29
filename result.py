s1=int(input())
s2=int(input())
s3=int(input())
s4=int(input())
s5=int(input())
s6=int(input())

total=s1+s2+s3+s4+s5+s6

per=(s1+s2+s3+s4+s5+s6)/6
print("total:",total)
print("per:",per)
if s1>=35 and s2>=35 and s3>=35 and s4>=35 and s5>=35 and s6>=35:
    if per>=75:
        print("dict")
    elif per>=60:
        print("first")
    elif per>=50:
        print("second")
    else:
        print("third")
else:
    print("fail")
    
