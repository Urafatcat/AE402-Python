grade=input("what is your grade")
grade=int(grade)
if(not(grade>0 and grade<100)):
    print("reenter score")
elif grade>=90:
    print("you got an A")
elif grade>=80:
    print("you got a B")
elif grade>=70:
    print("you got a C")
elif grade>=60:
    print("you got a D")
else:
    print("fail")
