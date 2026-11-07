# exception_handling.py
import sys

# Handling division by zero
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Handling multiple exceptions
# Pass the number as an argument (python exception_handling.py 5) or type it when asked.
try:
    raw = sys.argv[1] if len(sys.argv) > 1 else input("Enter a number: ")
    num = int(raw)
    result = 10 / num
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except EOFError:
    print("No input provided.")
else:
    print(f"10 / {num} = {result}")
finally:
    print("Execution completed.")
