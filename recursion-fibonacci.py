
# Python program to display the Fibonacci sequence

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n - 1) + recur_fibo(n -2 ))


n = int(input("Enter any number: "))

# check if the number of terms is valid
if n <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(n):
       print(recur_fibo(i))