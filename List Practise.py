# List Practise.py
numbers = [5, 2, 1, 7, 4, 5, 5, 5]

numbers.append(12)  # .append(object) enters a new object at the end of the list.
numbers.insert(0, 20)  # .insert(position, object) enters an object at the required index.
numbers.remove(2)  # .remove(object) removes the object entered.
numbers.pop()  # .pop() removes the last item in the list.
# numbers.clear()  # .clear() clears the whole list and makes it an empty list.
numbers.index(5)  # .index(object) shows the index of the required object.
numbers.count(5)  # .count(object) shows how many of that object are in the list
numbers.sort()  # .sort() sorts the list in ascending order
numbers.reverse()  # .reverse() reverses the list order
numbers2 = numbers.copy()  # .copy() copies the list, and assigns it to another list, numbers2[]
print(numbers)
print(numbers.index(5))
print(numbers.count(5))

# Checking for an item in a list, which returns True if it is or False if it is not.
print(50 in numbers)

numbers3 = [2, 2, 3, 2, 2, 3, 4, 5, 53, 3, 43, 3, 2, 2, 3, 4]
print(numbers3)
unique_numbers = []
for number in numbers3:
    if number not in unique_numbers:
        unique_numbers.append(number)
print(unique_numbers)
