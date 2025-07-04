#Remove the first n characters from a string.

text = input("Enter teh string : ")
n = int(input("Enter n : "))
result = text[n:]   # Slice from index n to end
print("Result : ",result)