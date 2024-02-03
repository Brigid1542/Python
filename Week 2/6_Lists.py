# Lists are mutable
list1 = [1, 2, 3, 4, 5]
print(*list1)
print(list1[3])
# Adding to list
print(list1, sep=" ")
list1.insert(len(list1), 6)
print(list1, sep=" ")
list1.append(7)
print(list1, sep=" ")
list1.extend([8, 9, 10])
print(list1, sep=" ")
# Removing something from a list
list1.pop(4)
print(list1, sep=" ")
del list1[2]
print(list1, sep=" ")
# Iteration in lists
for x in list1:
    print(x)
list2 = ['A', 'B', 'C', 'D']
print(list2)
list3 = ['A', 2, 'G', 'R', 8]
print(list3)
