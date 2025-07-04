def Remove_all_of_the_vowels() :
    string = "Practice Problems to Drill List Comprehension in Your Head."
    new_str = " "
    for i in string:
        if i.lower() not in 'a e i o u':
            new_str = new_str + i

    print("The new string without vowels : ", new_str)

Remove_all_of_the_vowels()
