english=input("what is ur english score?")
math=input("what is ur math score?")
english=int(english)
math=int(math)
if english>=90 and math>=90:
    print("you get a prize")
elif english<60 and math>=60:
    print("try harder!")
elif math<60 and english>=60:
    print("try harder")
else:
    print("you get punishment")