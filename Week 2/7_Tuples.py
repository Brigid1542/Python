# Tuples are immutable
my_tuple = (1, 'String', 4.5, True, 'String')
print(my_tuple[1])
print(type(my_tuple))
print(my_tuple.count('String'))
print(my_tuple.index(4.5))
# Iteration in tuples
for x in my_tuple:
    print(x)