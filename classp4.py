#Annuity plan

PMT=input("what is your PMT: ")
r = input("Rate(r): ")
n = input("the number of times that interest is compounded(n): ")
t = input("the time the money is invested(t): ")
x=input("What is this: ")

print("A = ",int(PMT)*int(x)*((((1+(int(r)/int(n)))**(int(n)*int(t))-1))/(int(r)/int(n))))