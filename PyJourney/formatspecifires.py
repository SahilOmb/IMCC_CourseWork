# =====================================================================
# FORMAT SPECIFIERS IN PYTHON
# =====================================================================
# Used inside f-strings to format text alignment, padding, and numbers.
# Syntax: {variable:specifier}
# =====================================================================

price = 3.14159
big_number = 1000000
percentage = 0.75
text = "Code"

# ---------------------------------------------------------------------
# 1. FLOATING POINT PRECISION (Rounding decimals)
# ---------------------------------------------------------------------
# Use '.Nf' where N is the number of decimal places to keep
print(f"Original: {price}")        # Output: 3.14159
print(f"Rounded:  {price:.2f}")     # Output: 3.14 (Rounds to 2 decimal places)
print(f"Rounded:  {price:.0f}")     # Output: 3    (Rounds to a whole number)

# ---------------------------------------------------------------------
# 2. NUMBER FORMATTING (Commas and Signs)
# ---------------------------------------------------------------------
# Use ',' to automatically add thousands separators
print(f"Big Number: {big_number:,}") # Output: 1,000,000

# Use '+' to always show the sign (positive or negative)
print(f"With Sign:   {price:+.2f}")   # Output: +3.14

# ---------------------------------------------------------------------
# 3. PERCENTAGES
# ---------------------------------------------------------------------
# Use '%' to multiply by 100 and add the percentage sign automatically
print(f"Progress: {percentage:%}")   # Output: 75.000000%
print(f"Progress: {percentage:.0f%}") # Output: 75%

# ---------------------------------------------------------------------
# 4. PADDING AND ALIGNMENT (Great for written exams!)
# ---------------------------------------------------------------------
# Use '<' for Left, '>' for Right, and '^' for Center alignment.
# The number following the symbol specifies the total width of the block.

print(f"Left:   '{text:<10}'")  # Output: 'Code      ' (padded on right)
print(f"Right:  '{text:>10}'")  # Output: '      Code' (padded on left)
print(f"Center: '{text:^10}'")  # Output: '   Code   ' (centered)

# You can also specify a character to fill the empty space instead of spaces:
print(f"Fill:   '{text:*^10}'")  # Output: '***Code***'
