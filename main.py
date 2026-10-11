import utility_module as utils


def main():
    print("=" * 40)
    print("       PYTHON UTILITY MODULE")
    print("=" * 40)

    # Email validation
    email = input("\nEnter your email: ").strip()

    if utils.is_valid_email(email):
        print("Email: Valid")
    else:
        print("Email: Invalid")

    # Number validation and currency formatting
    amount = input("\nEnter an amount in rupees: ").strip()

    if utils.is_valid_number(amount):
        amount = float(amount)

        if amount >= 0:
            print("Formatted amount:", utils.format_currency(amount))
        else:
            print("Amount cannot be negative.")
    else:
        print("Please enter a valid number.")

    # Percentage calculation
    try:
        value = float(input("\nEnter obtained marks: "))
        total = float(input("Enter total marks: "))

        if value < 0 or total <= 0 or value > total:
            print("Please enter valid marks.")
        else:
            percentage = utils.calculate_percentage(value, total)
            print(f"Percentage: {percentage:.2f}%")

    except ValueError:
        print("Please enter valid numeric values.")

    # Current date
    print("\nToday's date:", utils.get_current_date())

    # File utility example
    filename = "sample.txt"
    content = "Python Utility Module is working successfully!"

    utils.write_text_file(filename, content)
    print("\nText file created successfully.")

    print("File content:", utils.read_text_file(filename))

    print("\nProgram completed successfully!")


if __name__ == "__main__":
    main()