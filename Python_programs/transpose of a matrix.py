matrix1=[[2*x for x in range(1,4)],[3*x for x in range(1,4)],[5*x for x in range(2,5)]]
matrix2=[[2*x for x in range(4,1,-1)],[3*x for x in range(2,5)],[7*x for x in range(2,5)]]
result=[[0 for x in range(3)] for x in range(3)]
#transpose=[[x[i]for  x in matrix] for i  in range (3)]
for i in range (3):
    for j in range (3):
        #for k in range (3):
        result[i][j]=matrix1[i][j]+matrix2[i][j]
            
    
print(matrix1)
print(matrix2)
print(result)
