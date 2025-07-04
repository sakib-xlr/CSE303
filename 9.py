def largest_num_119(list):
    largest = list[0]

    for i in list:
        if i > largest:
            largest = i
        return largest

def smallest_num_119(list):
    smallest = list[0]

    for i in list:
        if i < smallest:
            smallest = i
        return smallest

user_input = input("Enter numbers separeted by space : ")
numbers = [int(i)
           for i in user_input.split() ]

print("Larfest : ",largest_num_119(numbers))
print("Smaleest : ",smallest_num_119(numbers))


#user_input.split() Splits the input string (e.g., "10 20 30") into a list of strings:
