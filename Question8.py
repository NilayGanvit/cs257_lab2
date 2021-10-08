# Question 8
print("Enter the number to be checked")
a = int(input())
is_prime = True
for i in range(2, a):
    if a%i == 0:
        is_prime = False
if is_prime:
    print('Number is prime')
else:
    print('Number is not prime')