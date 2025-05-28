print("\n=== Type Conversion ===")

# Automatic type promotion
result = 3 + 4.5
print(f"{result}")
print(f"result is {type(result)}")

# Manual type conversion
float_num = 3.7
int_from_float = int(float_num)
print(f"int(3.7) = {int_from_float}")

int_num = 5
float_from_int = float(int_num)
print(f"float(5) = {float_from_int}")   # 5.0

# Rounding
import math
print(f"round(3.7) = {round(3.7)}") # 4
print(f"math.floor(3.7) = {math.floor(3.7)}") # 3(floor)
print(f"math.ceiling(3.2) = {math.ceil(3.2)}") # 4(ceil)