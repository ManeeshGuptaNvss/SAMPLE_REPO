a=[]
b=[]
c=[]

n=int(input('enter no. of subjects:'))
for i in range(0,n):
    x=int(input("enter points:"))
    y=int(input("enter credits:"))
    a.append(x)
    b.append(y)
for k in range(0,n):  
    z=(a[k]*b[k])
    print(z)
    c.append(z)
s=sum(c)
cgpa=s/25
print("CGPA is:",cgpa)
      
