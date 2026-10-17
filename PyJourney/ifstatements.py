age = 22
has_coffee = True

# Using 'and'
if age >= 18 and has_coffee:
    print("Ready for a late-night debugging session!")

# Using 'or'
is_weekend = False
if is_weekend or has_coffee:
    print("Code production is high.")

# Using 'not'
is_bug_fixed = False
if not is_bug_fixed:
    print("Keep searching the logs.")

score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")  # This block will execute
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

status = "Adult" if age >= 18 else "Minor"
print(status)  # "Adult"
