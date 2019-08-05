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
for i in range(r):
    for j in range(c):
        b=[[0 for z in range(i)] for y in range(j)]
        for k in range(len(b)):
            for l in range(len(b[0])):
                b[k][l]=a[k][l]
        pm(b)
        print('--------------------------------------------------------------------------------------------')
