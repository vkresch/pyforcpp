# Exception Handling
x, y = 5, 0

# Use assert to check if conditions are met
assert y != 0, "y cannot be zero"

# Use simple if statement to check conditions and raise errors
if y == 0:
    raise ZeroDivisionError("y is not allowed to be 0")

# Simple try catch
try:
    z = x / y

except ZeroDivisionError as e:
    print("Divide by zero error")
    print(e)

else:
    print("Else executed")

finally:
    print("Final line executed")
