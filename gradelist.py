n=int(input("How many people do you have"))
score=[]
lowest=100
highest=0
highestname=""
lowestname=""
summath=0
for i in range(0,2*n):
    mathscore=input("what is your name and score")
    score.append(mathscore)
    print(score)
    if i%2==1:
        score[i]=int(score[i])
        summath=summath+score[i]
        if highest<score[i]:
            highest=score[i]
            highestname=score[i-1]
        if lowest>score[i]:
            lowest=score[i]
            lowestname=score[i-1]
print(highest,highestname)
print(lowest,lowestname)
print("avg",summath/n)
    

