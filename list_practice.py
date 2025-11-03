# list- create, add items to the list, del items from the list, modify an element in the list, slicing in the list
# fun - length of a list, max value in the list, min value in the list

# create lists
colors_list = ["red", "blue", "orange", "green"]
sqrt_list = [1, 4, 9, 25, 36, 49]
print(f"colors list is {colors_list}")
print(f"sqrt list is {sqrt_list}")

# add items to the list
colors_list.append("purple")
sqrt_list.append("64")
print(f"colors list after adding itmes is => {colors_list}")
print(f"sqrt list after adding items is=> {sqrt_list}")

#del items from a list
del colors_list[0]
del sqrt_list[0]
print(f"colors list after deleting the 1st item is => {colors_list}")
print(f"sqrt list after deleting the 1st item is=> {sqrt_list}")
