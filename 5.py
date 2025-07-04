def prime_checker_119(N):
    if N <= 1 :
        return False
    for i in range (2 , int( N ** 0.5) + 1 ):
        if N % i == 0:
            return False
    return True
num = int(input("Enter the number : "))
if prime_checker_119(num):
    print(num , "is prime")
else:
    print(num , "is not prime")