# For Loop Practise.py

for item in range(5, 10):
    print(item)

for item in range(0, 10):
    print(item)

prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"Total: ${total}")

for x in range(4):
    for y in range(4):
        print(f"({x}, {y})")

# Normal way of printing an 'F' with 'x's.
numbers = [5, 2, 5, 2, 2]
for number in numbers:
    output = ''
    for count in range(number):
        output += 'x'
    print(output)

# Python way of an 'F' with 'x's because you can multiply string by a certain number to produce multiple strings
numbers = [5, 2, 5, 2, 2]
for number in numbers:
    print('x' * number)

names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names[:])

# Finding the largest number in an array.
numbers1 = [3, 6, 2, 8, 4, 10]
max = numbers1[0]
for number in numbers1:
    if number > max:
        max = number
print(max)

# 2D Arrays
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)