principal = int(input("How much was deposited in the account: "))
rate = int(input("Interest rate: "))
compound = int(input("How many times per year is it compounded: "))
years = int(input("For how many years would the interest compound: "))

amount = 1 + rate/(100*compound)
compound_interest = principal * amount**(years*compound)

print(compound_interest)
