if __name__ == '__main__':
    k=[]
    for i in range(int(input())):
        name = input()
        score = float(input())
        k.append([name,score])
    max1=0
    for i in range(len(k)):
        if max1<k[i][1]:
            max1=k[i][1]
print(max1)
