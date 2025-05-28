from fractions import Fraction

# Create fractions
half = Fraction(1,2) 
third = Fraction(1,3)
quarter = Fraction(1, 4)

print(f"1/2 = {half}")
print(f"1/3 = {third}")  
print(f"1/4 = {quarter}")

# Fraction arithmetic
result = half + third
print(f"1/2 + 1/3 = {result}")

# Convert from decimal
decimal_frac = Fraction(0.75)
print(f"0.75 as fraction: {decimal_frac}") # 3/4

# From string
string_frac = Fraction("3/7")
print(f"3/7 = {string_frac}")