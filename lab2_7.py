def Find_divisible_by_2_to_9():
    numbers = [i for i in range(1, 1001)]
    div_by_2_to_9 = []
    for i in numbers:
        for j in range(2,9):
            if i % j == 0:
                div_by_2_to_9.append(i)

    print("The numbers divisible by 2 to 9 : ",div_by_2_to_9)

Find_divisible_by_2_to_9()
