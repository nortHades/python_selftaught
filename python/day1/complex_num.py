# Create complex numbers using j or J suffix
z1 = 3 + 5j                    # 3 + 5i in mathematical notation
z2 = 2 - 4J                    # 2 - 4i  
z3 = complex(1, 2)             # 1 + 2i using complex() function

print(f"z1 = {z1}")
print(f"z2 = {z2}")
print(f"z3 = {z3}")

# Complex number operations
addition = z1 + z2
multiplication = z1 * z2
print(f"z1 + z2 = {addition}")
print(f"z1 * z2 = {multiplication}")

# Access real and imaginary parts
print(f"Real part of z1: {z1.real}")      # 3.0
print(f"Imaginary part of z1: {z1.imag}") # 5.0

# Complex number methods
print(f"Conjugate of z1: {z1.conjugate()}")  # 3 - 5j
print(f"Absolute value of z1: {abs(z1)}")    # 5.830951894845301