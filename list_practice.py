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

# modify an element
colors_list[0] = "yellow"
sqrt_list[0] = 2
print(f"colors list after modifying the 1st item is => {colors_list}")
print(f"sqrt list after modifying the 1st item is=> {sqrt_list}")

# slicing in a list
print(f"slicing the colors_list => {colors_list[0:3]}")
print(f"slicing the sqrt_list => {sqrt_list[1:3]}")

# length of a list
print(f"the length of color_list is => {len(colors_list)}")
print(f"the length of sqrt_list is => {len(sqrt_list)}")