from enum import nonmember


def Highest_divisors_list():
    numbers = [i for i in range(1, 1001)]
    highest_divisors  = []

    print(f"{'Number':<7} : {'Highest Divisor'}")
    print('-' * 25)

    for i in numbers:
        highest = None
        for j in range(2,10):
            if i % j == 0:
                if highest is None   or    j > highest:
                    highest = j
        highest_divisors.append(highest)

        print(f"{i:<7} : {highest}")

Highest_divisors_list()