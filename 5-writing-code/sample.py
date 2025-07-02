# sample.py: Program to add two numbers entered by the user

def get_number(prompt: str) -> float:
    """Prompt the user for a number and validate input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main() -> None:
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is {result}.")

if __name__ == "__main__":
    main()



