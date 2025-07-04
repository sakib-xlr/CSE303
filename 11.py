#Display characters at even indexes (0, 2, 4...) of a string.

text = input("Enter a string")
result = text[::2]      #start at 0 , step by 2
print("Even index carecters : ",result)



#text[::2] slices the string with step size 2......Example: "Python" → "Pto".