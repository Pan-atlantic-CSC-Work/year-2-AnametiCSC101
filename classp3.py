#compound Interest


p = input("Principal(p): ")
r = input("Rate(r): ")
n = input("the number of times that interest is compounded(n): ")
t = input("the time the money is invested(t): ")

ans=int(p)*(1+(int(r)/int(n)))**(int(n)*int(t))
print("A = ",ans)