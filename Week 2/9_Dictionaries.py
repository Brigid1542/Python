sample_dict = {1: 'Coffee', 2: "Tea", 3: "Cocoa", 4: "Juice"}
print(sample_dict)
sample_dict[2] = "Mint Tea"
print(sample_dict)
for key, value in sample_dict.items():
    print(str(key) + " : " + value)
del sample_dict[3]
print(sample_dict)
print(type(sample_dict))
