numbers = [i for i in range(1, 1001)]
string = "Practice Problems to Drill List Comprehension in Your Head."


def Divisible_by_8(nums):
    div_by_8 = []
    for i in nums:
        if i % 8 == 0:
            div_by_8 = div_by_8 + [i]
    return div_by_8


def Have_6(nums):
    have_6 = []
    for i in nums:
        if '6' in str(i):
            have_6 = have_6 + [i]
    return have_6


def Number_of_spaces(s):
    count_space = 0
    for i in s:
        if i == ' ':
            count_space += 1
    return count_space


def Remove_all_of_the_vowels(s):
    new_str = ""
    for i in s:
        if i.lower() not in 'aeiou':
            new_str = new_str + i
    return new_str


def Words_less_than_5_letters(s):
    new_str = s.split()
    short_words = []
    for i in new_str:
        if len(i) < 5:
            short_words.append(i)
    return short_words


def Count_length_of_each_word(s):
    new_str = s.split()
    word_length = []
    for word in new_str:
        word_length.append(len(word))

    result = []
    for i in range(len(new_str)):
        result.append(f"{new_str[i]}: {word_length[i]}")
    return result


def Find_divisible_by_2_to_9(nums):
    div_by_2_to_9 = []
    for i in nums:
        for j in range(2, 9):
            if i % j == 0:
                div_by_2_to_9.append(i)
                break
    return div_by_2_to_9


def Highest_divisors_list(nums):
    highest_divisors = []
    print(f"{'Number':<7} : {'Highest Divisor'}")
    print('-' * 25)

    for i in nums:
        highest = None
        for j in range(9, 1, -1):  # Check from 9 down to 2
            if i % j == 0:
                highest = j
                break
        highest_divisors.append(highest)
        print(f"{i:<7} : {highest}")
    return highest_divisors



print("Numbers divisible by 8:", Divisible_by_8(numbers))
print("\nNumbers containing '6':", Have_6(numbers))
print("\nNumber of spaces in string:", Number_of_spaces(string))
print("\nString without vowels:", Remove_all_of_the_vowels(string))
print("\nWords with less than 5 letters:", Words_less_than_5_letters(string))
print("\nLength of each word:")
for item in Count_length_of_each_word(string):
    print(item)
print("\nNumbers divisible by 2-9:", Find_divisible_by_2_to_9(numbers))
print("\nHighest divisors for numbers 1-1000:")
Highest_divisors_list(numbers[:20])