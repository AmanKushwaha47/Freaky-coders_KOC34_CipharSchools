import random
n=random.randint(-11,20)
c=0
if n>0:
    print(n,"is a positive number")
elif n<0:
    print(n,"is a negative number")
else:
    print("It is 0")
if n%2==0:
    print(n,"is an even number")
else:
    print(n,"is a odd number")
if n>1:
    for i in range(2,n):
        if n%i==0:
            c=c+1
    if c==0:
        print(n,"is a prime number")
    else:
        print(n,"is a composite number")
else:
    print("neither prime nor composite")
print("Thank You!")
