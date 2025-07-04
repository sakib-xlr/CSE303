def Count_length_of_each_word():
    string = "Practice Problems to Drill List Comprehension in Your Head."

    new_str = string.split()
    word_length = [ ]

    for word in new_str:
        word_length .append(len(word))

    for i in range(len(new_str)):
        print(new_str[i], ":", word_length[i])


Count_length_of_each_word()
