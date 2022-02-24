record={"zion":3,"james":4,"nicole":4,"kemi":5,"clinton":4,"timi":7,"temi":5,"mimi":6,"tolu":4}

std=str(input("student name: "))
def score(std):
    for x in record.keys():
        if(std==x):
            print("students score is " + str(record[std]))
            break
        else:
            print("This student didn't write the CA")
            break
    
score(std)