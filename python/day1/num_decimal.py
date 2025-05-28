from decimal import Decimal

# Regular float has precision issues
regular_calc = 0.1 + 0.1 + 0.1
print(f"Regular float: {regular_calc}") 

# Decimal provides exact decimal arithmetic  
decimal_calc = Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
print(f"Deciaml float: {decimal_calc}") 

# Financial calculations
price = Decimal('19.99')
tax_decimal = Decimal('0.08')
tax = price * tax_decimal # $1.5992
total = price + tax # $21.5892
print(f"Price: ${price}")
print(f"Tax: ${tax}")
print(f"Total: ${total}")