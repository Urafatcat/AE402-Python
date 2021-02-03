
names=list()
scores=list()
avg=0

def average(scores):
    total=0
    n=len(scores)
    for item in range(n):
        total=total+scores[item]
    average=total/n
    return average

def highest(scores, names):
    highest=0
    highestname=""
    n=len(scores)
    for i in range(n):
        if scores[i]>highest:
            highest=score[i]
            highestname=names[i]
        person=list()
        person.append(highestname)
        person.append(highest)
        return person
   
def lowest(scores,names):
    lowest=100
    lowestname=""
    n=len(scores)
    for i in range(n):
        if scores[i]<lowest:
            lowest=score[i]
            lowestname=names[i]
        person=list()
        person.append(lowestname)
        person.append(lowest)
        return person
n=input("how many people in this class")
n=int(n)

for i in range(n):
    name=input("please in put name")
    names.append(name)
    score=input("please input score")
    score=int(score)
    scores.append(score)

avg = average(scores)
print(avg)
hi=highest(scores, names)
print(hi)
low=lowest(scores,names)
print=(low)
