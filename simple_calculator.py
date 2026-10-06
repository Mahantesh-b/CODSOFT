"""Simple Calculator - CODSOFT Python Internship Project."""

def get_number(prompt):
    """Read and validate a numeric value from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def calculate(first, second, operation):
    """Perform a calculation and return the result."""
    if operation == "1":
        return first + second
    if operation == "2":
        return first - second
    if operation == "3":
        return first * second
    if operation == "4":
        if second == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return first / second
    raise ValueError("Invalid operation.")


def main():
    """Run the calculator application."""
    operations = {
        "1": ("Addition", "+"),
        "2": ("Subtraction", "-"),
        "3": ("Multiplication", "*"),
        "4": ("Division", "/"),
    }

    print("\n=== Simple Calculator ===")

    while True:
        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Choose an operation: ").strip()

        if choice == "5":
            print("Thank you for using the calculator!")
            break

        if choice not in operations:
            print("Invalid choice. Please select 1-5.")
            continue

        first = get_number("Enter first number: ")
        second = get_number("Enter second number: ")

        try:
            result = calculate(first, second, choice)
            symbol = operations[choice][1]
            print(f"Result: {first:g} {symbol} {second:g} = {result:g}")
        except ZeroDivisionError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
