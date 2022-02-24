subjects = ["MAth","English","Chemistry","Physics","Data Processing"]
jamb = input("What is your Jamb score: ")
grades = []
count = 0
for i in range(len(subjects)):
    someone = input("What is your grade in "+subjects[i])
    grades.append(someone)
    
for i in grades:
    if(("A" or "B" or "C")in grades):
        count+=1
if(int(jamb)>=230 and count==5):
    print("You are admitted into Computer Science")
else:
    print("You aren't admitted into computer science, redo your exams")