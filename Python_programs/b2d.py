st=input('enter elements in Binary\n')
lis=list(st.split())
print(lis)
sr=''
for i in lis:
    sr+=chr(int(i,2))
print(sr)
