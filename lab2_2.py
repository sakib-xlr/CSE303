def Have_6():
    numbers = [i for i in range(1, 1001)]

    have_6 = []

    for i in numbers:
        if '6' in str(i):
            have_6 = have_6 + [i]

    print("The numbers that have 6 in them : ",have_6)

Have_6()