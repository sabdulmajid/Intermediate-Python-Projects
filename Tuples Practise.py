# Tuples Practise.py
# A tuple is an immutable list. This means that you cannot modify anything in in once done.
numbers = (1, 2, 3)
print(numbers[1])


# Unpacking: A powerful technique in Python that allows to assign more than 1 values to variables from a list.
coordinates = [1, 2, 3]
x, y, z = coordinates
print(x, y, z)

# The same code above can be written without 'unpacking' as:
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
print(x)
print(y)
print(z)