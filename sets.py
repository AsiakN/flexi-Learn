# A set is an unordered collection with no duplicates
# Basic use of sets include membership testing and eliminating duplicates in lists
# Sets can also implement mathematical operations like union, intersection etc

# You can create a set using set() or curly braces. You can only create an empty set using the set() method

# Another type of set exists called frozenset. Frozenset is immutable but set is mutable

basket = {'Apple', 'Banana', 'Avocado', 'pineapple', 'Apple', 'Orange'}
print(sorted(basket))

a = set('abracadabra')
b = set('alacazam')
print(a.intersection(b))
print(a | b)  # The " | " operator means or. It sums elements in both sets. Union operation
print(a & b)  # The " &" operator means and . It finds the elements in both a and b. Intersection operation
print(a ^ b)   # The " ^ " operator means not. Finds the elements in one set but not in the other set. Symmetric difference
print(a.isdisjoint(b))
print(b.issubset(a))
# SET COMPREHENSIONS

s = {x for x in 'abracadabra' if x not in 'abc'}
print(s)
# METHODS IN SETS
# 1. UNION
    #SYNTAX
        # setA.union(setB)
# 2. INTERSECTION
    # SYNTAX
        # setA.intersection(setB)
# 3. DIFFERENCE
     # SYNTAX
        # setA.difference(setB)
# 4. SYMMETRIC DIFFERENCE
    # SYNTAX
        # setA.symmetric_difference(SetB)
# 5. DISJOINT
    # SYNTAX
        # setA.isdisjoint(setB)
        # Returns true or false value
# 6. SUBSET
    # SYNTAX
        # setA.issubset(setB)
        # Returns true or false value
# 7. SUPERSET
    # SYNTAX
        # setA.issuperset(setB)
        # Returns true or false value
# 8. PROPER SUBSET/SUPERSET

# MODIFYING SETS
# 1. set.add(element)
# 2. set.remove(element)
# 3.  Set.discard(element)
# 4. set.pop()
# 5. set.clear()

numbers = { 24, 67, 89,90, 78,78, 24 }
print(sum(numbers))
print(len(numbers))