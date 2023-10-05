shares = 2000
unit_cost = 40
total_cost = unit_cost * shares
commission1 = 0.03 * total_cost

unit_sales = 42.75
total_sales = unit_sales * shares
commission2 = 0.03 * total_sales

balance = total_sales - (total_cost + commission1 + commission2)
if balance > 0:
    print(f"Joe made a profit of ${balance}")
else:
    print("Joe had a loss")
print(f'''He paid ${total_cost} for the stocks and paid his broker a commission of ${commission1} when he bought them.
Joe sold them 2 weeks after at a total of ${total_sales} and paid his broker ${commission2}.
''')
