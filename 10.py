user_input = input("Enter numbers separeted by space : ")
numbers = [int(i)
           for i in user_input.split() ]

if len(numbers) < 2:
    print("Need atleast 2 numbers : ")
else:
    largest = second = float('-inf')
    for n in numbers:
        if n > largest:
            second = largest
            largest = n
        elif n > second and n != largest:
            second = n
    print("Second largest number :", second)




    #float('-inf') in Python represents negative infinity, a special floating-point value that is smaller than any other number (including all negative numbers)