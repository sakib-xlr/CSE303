list1 = [1, 2, 3, 4, 5]
list2 = [10, 11, 12, 13, 14]

new_list = [x for x in list1 if x % 2 != 0] + [x for x in list2 if x % 2 == 0]
print("New list:", new_list)