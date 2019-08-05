year=int(input())

if year%4 is 0:
    if year% 100 is 0 and year % 400 is 0 :
        print("a leap year")
    elif year% 100 is 0 and year % 400 is not 0 :
        print('not a leap year')
    else :
        print('a leap year')
else:
    print('not a leap year')
