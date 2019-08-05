marks=[]
n=int(input('enter number of subjects:'))
for i in range (0,n):
    x=int(input('enter subject marks:'))
    marks.append(x)
print(marks)
total=(sum(marks))
p=total/(n*100)
flag=0
for i in range(0,n):
    if marks[i]<35:
        flag=flag+1
if flag==0:
    if p>=0.6 :
         print('Grade-A')
    elif p>=0.5 and p<0.6:
      print('Grade-B')
    elif p>=0.4 and p<0.5:
        print('Grade-C')
    elif p>=0.35 and p<0.4:
        print('Grade-D')
    else:
        print("Failed!")
else:
    print("no minimum marks in",flag," subject(s)")
