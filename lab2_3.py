def Number_of_spaces ():
    string = "Practice Problems to Drill List Comprehension in Your Head."

    count_space = 0

    for i in string:
        if i == ' ':
            count_space += 1

    print("The spaces in the given string is, ",count_space)

Number_of_spaces()
