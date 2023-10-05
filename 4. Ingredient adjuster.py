name = input("What's your name: ")
no_of_cookies = int(input(f"Hi {name}, how many cookies do you want to make: "))

sugar = (1.5/48) * no_of_cookies
butter = (1/48) * no_of_cookies
flour = (2.75/48) * no_of_cookies

print(f'''You'll need {round(sugar, 4)} cups of sugar,
{round(butter, 4)} cups of butter
and {round(flour, 4)} cups of flour''')
print("Happy Baking!")