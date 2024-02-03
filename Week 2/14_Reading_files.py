with open('file.txt', mode='r') as file:
    data = file.readlines()
    for x in data:
        print(x)

