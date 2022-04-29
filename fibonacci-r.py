def fibonacci(a):  
   if a <= 1:  
       return a  
   else:  
       return(fibonacci(a-1) + fibonacci(a-2))  
terms = int(input("select range of numbers for Fibonacci series? "))  
if terms <= 0:  
   print("Not a valid number")  
else:  
   print("Fibonacci sequence:")  
   for i in range(terms):  
       print(fibonacci(i))  
       