# Question 5
print("Enter the Index of the Fibonacci number") 
n = int(input())
a = 0
b = 1
if n == 1:
    print(0)
elif n==2:
    print(1)
else:
    for i in range(n-2):
        a,b=b,a+b
    print(b)
