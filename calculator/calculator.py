# Function to perform addition operation
def add(x, y):
    return x + y

# Function to perform subtraction operation
def subtract(x, y):
    return x - y

# Function to perform multiplication operation
def multiply(x, y):
    return x * y

# Function to perform division operation
def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    else:
        return x / y

# Main function to manage the application flow
def main():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter your choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", add(num1, num2))
    elif choice == "2":
        print("Result:", subtract(num1, num2))
    elif choice == "3":
        print("Result:", multiply(num1, num2))
    elif choice == "4":
        print("Result:", divide(num1, num2))
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
