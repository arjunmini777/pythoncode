# 1. Create a list of names and print the second item.
list_1 = ["James", "Daniel", "Jordan"]
print(list_1[1])

# 2. Create a list of sports and then replace the second item with another sport.
list_sports = ["soccer", "basketball", "baseball"]
list_sports[1] = "cricket"
print(list_sports)

# 3. Create a list containing numbers and delete the fifth number from the array.
list_num = [14, 15, 12, 18, 46, 62, 90]
del list_num[4]
print(list_num)

# 4. Create two lists of numbers and merge them.
list_num2 = [5, 10, 15, 20]
list_num3 = [3, 6, 9, 12]
list_num4 = list_num2 + list_num3
print(list_num4)

# 5. Create a list of numbers and find the length, minimum, and maximum.
list_num5 = [7, 3, 4, 9, 6, 1, 3, 2]
print(f"The max number in list_num5 is => {max(list_num5)}")
print(f"The min number in list_num5 is => {min(list_num5)}")
print(f"the length of list_num5 is => {len(list_num5)}")
# 6. Create a dictionary of students and scores and print out a student’s score.
dict_1 = {"Bob": 95, "Mary": 98, "Marcus": 89}
print(dict_1["Bob"])

# 7. Create a dictionary with the key being names and values being ages and then delete the second key/value pair.
dict_2 = {"Jimmy": 55, "James": 67, "Joquain": 45}
del dict_2["James"]
print(dict_2)

# 8. Create a dictionary of names and ages and then print out all the keys and values
dict_3 = {"Jimmya": 55, "Jamesa": 67, "Joquaina": 45}
print(dict_3)

# 9. Create a tuple of your favorite movies
tup_1 = ("The grinch", "Matilda", "Home alone")
print(f"My fav movies are => {tup_1}")

# 10. Create a tuple and print all the items from the first to third index.
tup_2 = (10, 28, 56, 73, 67)
print(tup_2[1:4])
