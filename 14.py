def palindrome_checker_119(s):
    return s == s[::-1]

text = input("Enter a string: ")
if palindrome_checker_119(text):
    print("It's a palindrome!")
else:
    print("Not a palindrome.")