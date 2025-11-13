# Create a list and print it with for loop
list_1 = ["Orange", "Yellow", "Brown", "Green", "Red"]
for x in list_1:
    print(x)

# Now find the range of a number saying which number is even or odd
for y in range(1,301):
    if y % 2 == 0:
        print(f"{y} ==> This is an even number")
    else:
        print(f"{y} ==> This is an odd number")

# Do the range of a number
for z in range(0,1001,6):
    print(f"The pattern starting from 0 and adding 6 each time until 1000 is ==> {z}")
