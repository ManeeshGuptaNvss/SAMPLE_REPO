def pm(r):
    for i in range(len(r)):
        for j in range(len(r[0])):
            print('\t',r[i][j],end='')
        print('\n')
r1=int(input("r1:"))
c1=int(input("c1:"))
r2=int(input("r2:"))
c2=int(input("c2:"))
if c1==r2:
    
    a=[[0 for i in range(c1)] for j in range(r1)]
    b=[[0 for i in range(c2)] for j in range(r2)]
    r=[[0 for i in range(c2)] for j in range(r1)]
    print('a')
    for i in range(r1):
        for j in range(c1):
            a[i][j]=int(input())
    print('b')
    for i in range(r2):
        for j in range(c2):
            b[i][j]=int(input())
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
              r[i][j]+=a[i][k]*b[k][j]
else:
    print('Invalid Matrix Multiplication')
pm(r)
