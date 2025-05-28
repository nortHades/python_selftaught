print("=== Practical Application Exercises ===")

# Exercise 1: Time conversion
total_seconds = 3661
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"{total_seconds} seconds = {hours} hours {minutes} minutes {seconds} seconds")

# Exercise 2: Pagination calculation
total_items = 127    # total items
items_per_page = 10  # items per page

total_pages = total_items // items_per_page
remaining_items = total_items % items_per_page
if remaining_items > 0:
    total_pages += 1

print(f"Total {total_items} items, {items_per_page} per page")
print(f"Need {total_pages} pages")
print(f"Last page has {remaining_items if remaining_items > 0 else items_per_page} items")

# Exercise 3: Compound interest calculation
principal = 10000    # principal
annual_rate = 0.05   # annual rate 5%
years = 10          # investment years

# Compound interest formula: A = P(1 + r)^t
final_amount = principal * (1 + annual_rate) ** years
interest_earned = final_amount - principal

print(f"Principal: ${principal}")
print(f"Annual rate: {annual_rate * 100}%")
print(f"Investment years: {years} years")
print(f"Final amount: ${final_amount:.2f}")
print(f"Interest earned: ${interest_earned:.2f}")