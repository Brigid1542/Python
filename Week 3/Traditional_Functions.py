my_list=[1,2,3]
def add_to_list(item):
    new_list=my_list.append(item)
    return new_list

print(add_to_list(4))
print(my_list)