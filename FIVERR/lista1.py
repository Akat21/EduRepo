def print_hi():
    print("hi")

def zad1_4():
    print_hi()

def first_for(text):
    for i in range(6):
        print(text)

def first_while(text):
    x = 6
    while x > 0:
        print(text)
        x-=1

def zad1_7(x):
    if x % 2 == 0:
        return 1
    elif x % 2 == 1:
        return 0

def zad1_8():
    sum = 0
    for i in range(500):
        if i % 11 == 0:
            sum += i
            print(i)
    return sum

def zad1_9(x,n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return x * zad1_9(x,n-1) 

def zad1_10(a,b,c,d,e):
    nums = [a,b,c,d,e]
    print(sorted(nums)[-2])

#zad1_10(8,18,39,2,10)