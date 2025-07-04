def fibonacci(N):
    if N == 0 :
        return 0
    elif N == 1 :
        return 1
    A = 0
    B = 1

    for _ in range (2 , N+1 ):
        A = B
        B = A+B
    return B
num = int(input("Enter the number : "))
print(f"{num}th Fibonacci number is : ",fibonacci(num))