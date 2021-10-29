def status(marks):
    if marks>=35:
        s='p'
    else:
        s='F'
    return s
def find_grade(marks):##grade
    if marks>=75:
        g="A+"
    elif marks>=60:
        g="A"
    elif marks>=50:
        g="B"
    else:
        if status(marks)=='F':
            g='F'
        else:
            g="C"
    return g
def bl_count(s1,s2,s3,s4,s5,s6): ##backlog count
    c=0
    if status(s1)=='F':
        c+=1
    if status(s2)=='F':
        c+=1
    if status(s3)=='F':
        c+=1
    if status(s4)=='F':
        c+=1
    if status(s5)=='F':
        c+=1
    if status(s6)=='F':
        c+=1
    return c
def find_total(s1,s2,s3,s4,s5,s6):##total marks
    res=s1+s2+s3+s4+s5+s6
    return res
def find_per(total):##total percentage
    return total/6
def valid(s1,s2,s3,s4,s5,s6):
    if (s1>=0 and s1<=100) and (s2>=0 and s2<=100) and(s3>=0 and s3<=100) and(s4>=0 and s4<=100)and (s5>=0 and s5<=100) and (s6>=0 and s6<=100):
        return True
    else:
        return False
s1,s2,s3,s4,s5,s6=map(int,input().split())
if valid(s1,s2,s3,s4,s5,s6):
    print("english",s1,100,status(s1),find_grade(s1))
    print("telugu",s2,100,status(s2),find_grade(s2))
    print("hindi",s3,100,status(s3),find_grade(s3))
    print("maths",s4,100,status(s4),find_grade(s4))
    print("science",s5,100,status(s5),find_grade(s5))
    print("social",s6,100,status(s6),find_grade(s6))
    print(bl_count(s1,s2,s3,s4,s5,s6))
    total=find_total(s1,s2,s3,s4,s5,s6)
    per=find_per(total)
    bl=bl_count(s1,s2,s3,s4,s5,s6)
    print(bl,total,per,end=" ")
    if bl==0:
        print(find_grade(per))
    else:print("Fail")
else:
    print("no valid")
