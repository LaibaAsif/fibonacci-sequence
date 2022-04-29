t1=0
t2=1
a=0
num = int(input("Enter the Range for Fibonacci series"))
if num<=0:
    print("Not a valid number")
else:
    print("Fibonacci sequence:")
    while a < num:
        print(t1)
        t3 = t1+t2
        t1=t2
        t2=t3
        a+=1