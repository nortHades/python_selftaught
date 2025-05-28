# Task: Restaurant bill calculator
print("=== Restaurant Bill Calculator ===")

# Bill information
subtotal = 85.50      # subtotal
tax_rate = 0.08       # tax rate 8%
tip_rate = 0.18       # tip rate 18%
people_count = 4      # number of people

# Calculations
tax_amount = subtotal * tax_rate
tip_amount = subtotal * tip_rate
total_amount = subtotal + tax_amount + tip_amount

# Split the cost
per_person = total_amount / people_count

# Display results
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax ({tax_rate*100}%): ${tax_amount:.2f}")
print(f"Tip ({tip_rate*100}%): ${tip_amount:.2f}")
print(f"Total: ${total_amount:.2f}")
print(f"Per person: ${per_person:.2f}")

# If need integer split (avoid making change)
import math
per_person_rounded = math.ceil(per_person)
total_collected = people_count * per_person_rounded
extra_tip = total_collected - total_amount

print(f"\nSuggested per person: ${per_person_rounded}")
print(f"Total collected: ${total_collected}")
print(f"Extra tip: ${extra_tip:.2f}")