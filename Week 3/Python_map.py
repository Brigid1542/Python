subjects=["Mathematics", "English", "Kiswahili", "Biology", "Business Studies"]

def find_subject(subject):
    if subject[0]=='B':
        return subject

map_subjects=map(find_subject, subjects)
print(map_subjects)
for x in map_subjects:
    print(x)