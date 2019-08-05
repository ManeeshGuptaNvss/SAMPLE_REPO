b=[]
def pm(r):
    for i in range(len(r)):
        for j in range(len(r[0])):
                       print('\t',r[i][j],end=' ')
        print('\n')
r=int(input("Enter row:"))
c=int(input("enter column:"))
a=[[0 for i in range(c)] for j in range(r)]
for i in range(r):
    for j in range(c):
        a[i][j]=int(input())
pm(a)
print("the submatrices are:")
for i in range(len(a)):
    print(a[i])
for i in range (len(a)):
    for j in range(len(a[0])):
                   print(a[i][j])
for i in range(len(a[0])):
    for j in range(len(a)):
                   
                   x=a[j][i]
                   b.append(x)
    print(b)
    b=[]

