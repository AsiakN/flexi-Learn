# A dictionary is useful for storing key-value pairs. Keys are unique identifiers
# Dictionaries are indexed by keys which are immutable objects (ints strings, tuples)
# If a tuple contains a mutable object directly or indirectly, then it can not be used as a key
# Initialise an empty dictionary by using {}

# MAIN DICTIONARY OPERATIONS

# 1. storing some value with a key and extracting the value when given the key
# 2. Delete a key-value pair
# 3. If you store using a key that is already in use, the old value associated with the key is lost.

#. You can perform sorting on the dictionary using sorted()

#creating a dictionary

asiak = {'Nathaniel': 7, 'Angela': 10}
asiak['Roseline'] = 6
print(asiak)

print(sorted(asiak))

# Dict() constructor creates a dictionary from a list or another data type
family=dict([['Asiak', 56], ['Asaami', 40], ['Awontiirim', 20], ['Angela', 15], ['Roseline', 8]])

print(family)

# DICTIONARY COMPREHENSIONS
# Lists comprehensions use square braces but dictionary comprehensions and dictionaries in general use curly braces
squares = {x: x**2  for x in range(11)}
print(squares)
print(squares[10])


# LOOPING TECHNIQUES
# 1. You  can print key and value pairs using items () method

knights = {'Sir lancelot': 'The brave', 'Sir Archie': 'The swift', 'Sir Geoffrey': 'The dragon'}
for k,v in knights.items():
    print(k,v)


for i, v in enumerate(knights):
    print(i,v)

students = {'nat': [20,30,40], 'Nath': [60,80,45]}
print('{:.2f}'.format((sum(students['nat'])/3)))
