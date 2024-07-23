# sample_error.py

def divide_numbers(num1, num2):
    """Divide num1 by num2 and return the result."""
    return num1 / num2

def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b

def main():
    try:
        # Intentional syntax error below
        result = divide_numbers(10, 0  # Missing closing parenthesis
        print("Division result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero!")
    
    # Intentional logic error
    total = add_numbers(10, "20")  # Adding integer and string
    print("Sum result:", total)

    # Intentional security issue
    sensitive_data = "password123"
    print(f"Sensitive data: {sensitive_data}")  # Sensitive data should not be printed

if __name__ == "__main__":
    main()
