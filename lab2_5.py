def Words_less_than_5_letters():
    string = "Practice Problems to Drill List Comprehension in Your Head."

    new_str = string.split()
    short_words = []
    for i in new_str:
        if len(i) < 5:
            short_words.append(i)
    print("The words less then 5 : ", short_words)


Words_less_than_5_letters()