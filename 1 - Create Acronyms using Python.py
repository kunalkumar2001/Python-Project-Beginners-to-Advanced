user_input = str(input("Enter sentence "))
text = user_input.split()

acronym = ""

for i in text:
    acronym = acronym + str(i[0]).upper()

print(acronym)