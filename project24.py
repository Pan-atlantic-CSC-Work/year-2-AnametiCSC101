record={"zion":"somethign","james":"someone","nicole":"clever","kemi":"password","clinton":"123456me","timi":"leaveme","temi":"wbjejqi","mimi":"hejqw","tolu":"wnqjen"}


u = str(input("Username: "))
p = str(input("Password: "))

def auth(user, pas):
    for x in record.keys():
        if(user==x and pas==record[user]):
            print("access granted")
            break
        else:
            print("No")
            break
    
auth(u,p)
            