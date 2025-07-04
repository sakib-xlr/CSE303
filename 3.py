def compound_interest_119() :
    P = float(input("Principle Amount : "))
    R = float(input("Interest Rate : "))
    T = float(input("Time in years : "))


    A = P * (1 + R / 100)**T

    print("Compound Amount " , A)

compound_interest_119()