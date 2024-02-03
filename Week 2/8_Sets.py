set_a = {1, 2, 3, 4, 5}
set_b ={ 4, 5, 6, 7, 8}
# Union of two sets
print(set_a | set_b)
print(set_a.union(set_b))
# Intersection of teo sets
print(set_a & set_b)
print(set_a.intersection(set_b))
# Set difference
print(set_a.difference(set_b))
print(set_a - set_b)
print(set_b.difference(set_a))
print(set_b - set_a)
# Symmetric difference
print(set_a.symmetric_difference(set_b))
print(set_a ^ set_b)
print(set_a)
print(type(set_a))
# Adding to the set
set_a.add(6)
print(set_a)
#  Removing from the set
set_a.remove(4)
print(set_a)
set_a.discard(3)
print(set_a)