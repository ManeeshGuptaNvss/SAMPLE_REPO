def fact(n):
    if n!=1 and n!=0:
        return n* fact(n-1)
    else:
        return 1
def exp(x,y):
    k=1
    for i in range(y):
        k*=x
    return k

#print(factorial(6))
n=eval(input('enter the value of n:'))
p=eval(input('enter the value of p:'))
r=eval(input('enter the value of r:'))
if n>r and 0<p<1:
    result=fact(n)/(fact(n-r)*fact(r))*(exp(p,r)*exp((1-p),(n-r)))
print(result)
