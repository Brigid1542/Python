try:

    with open("newfile.txt", mode='w') as file:
         file.writelines(["\nThis is another one to be added", "\nThis is another one "])
except FileNotFoundError as e:
    print(e, "File cannot be found")


