# Exercise on strings
first_name = input("Hi, what's your first name: ")
last_name = input("What's your last name: ")

initials = first_name.upper()[0] + "." + last_name.upper()[0]
full_name = first_name.capitalize() + last_name.upper()
username = first_name.upper()[0] + last_name

print(f"{initials}, {full_name}, {username.lower()}")
