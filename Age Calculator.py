from datetime import datetime

birth_str = input("Enter your birthdate (YYYY-MM-DD): ")

try:
    birth_date = datetime.strptime(birth_str, "%Y-%m-%d").date()
    today = datetime.today().date()

    if birth_date > today:
        print("You haven't been born yet! 👶")
    else:
        delta = today - birth_date
        years = delta.days // 365
        months = (delta.days % 365) // 30
        days = (delta.days % 365) % 30
        print(f"You are {years} years, {months} months, and {days} days old.")
except ValueError:
    print("Invalid date format. Please use YYYY-MM-DD.")


