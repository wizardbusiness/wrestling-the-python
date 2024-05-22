stuff_on_desk = ["cup", " puzzle box", "Guntz", "cat statue", "prayer plant", "keys"]

# can access from end of list with negative indexes
print(stuff_on_desk[-1]) 

# can slice list
print(stuff_on_desk[:3])
print(stuff_on_desk[3:])
print(stuff_on_desk[2:3])

# modify values by index
stuff_on_desk[-1] = "baubles"
print(stuff_on_desk)

# list operations

# extend
# extend with another list
stuff_on_desk.extend(["pen", "pocket knife", "back scratcher", "desk lamp", "notepad"])
print(stuff_on_desk)
# append 
# append an element to the list
stuff_on_desk.append("fireplace remote")
print(stuff_on_desk)
# insert
# insert an element at an index, pushing other values 1 to the right
stuff_on_desk.insert(1, "tissue")
print(stuff_on_desk)
# remove
# removes the element that matches the input
stuff_on_desk.remove("cup")
print(stuff_on_desk)

# pop 
# remove last element and return it

print(stuff_on_desk.pop())
print(stuff_on_desk)

# index get index of element that matches input if it exists, errors out if not
stuff_on_desk.index("prayer plant")

# count 
# counts the number of times an element matching the input appears in the list
print(stuff_on_desk.count("Guntz"))

# sort
# sorts a list in place
numbers = [1, 2, 4, -1, 3]
print(numbers)
numbers.sort()
print(numbers)

# copy
# copies a list
numbersC = numbers.copy()
numbersC.extend([3, 2, 20])
print(numbers)
print(numbersC)

# clear
# remove all elements
stuff_on_desk.clear()







