numbers = [12 , 34 , 53 , 67 , 89 , 67 , 98]
sum_even_index = 0

for i in range(0 , len(numbers) , 2):
    sum_even_index = sum_even_index + numbers[i]

print("Sum of even indexed elements : ", sum_even_index)


#The len(numbers) function in Python is used to get the length (the number of items)