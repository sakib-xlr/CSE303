def Divisible_by_8() :
    numbers = [ i for i in range ( 1 , 1001)]

    div_by_8 = []

    for i in numbers:
        if i % 8 == 0 :
            div_by_8 = div_by_8 + [i]

    print("The numbers that are divisible by 8 is : ",div_by_8)

Divisible_by_8()
