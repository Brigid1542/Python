subjects=["Mathematics", "English", "Kiswahili", "Biology", "Business Studies"]

def find_subject(subject):
    if subject[0]=='B':
        return subject

filter_subject = filter(find_subject, subjects)
print(filter_subject)
for x in filter_subject:
    print(x)