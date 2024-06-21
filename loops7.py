import calendar

# Input the year, month, start day, and number of days from the user
year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))
start_day = input("Enter the start day of the month (e.g., Monday, Tuesday, etc.): ")
num_days = int(input("Enter the number of days in the month: "))

# Create a dictionary to map day names to their corresponding index (0-6)
days_index = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6
}

# Get the index of the start day
start_day_index = days_index.get(start_day.capitalize(), -1)

if start_day_index == -1:
    print("Invalid start day input. Please enter a valid day name.")
else:
    # Create a calendar for the specified month
    cal = calendar.monthcalendar(year, month)
    
    # Print the calendar header
    print(f"Calendar for {calendar.month_name[month]} {year}:")
    print("Mo Tu We Th Fr Sa Su")
    
    # Initialize variables
    current_day = 1
    
    # Print the calendar
    for week in cal:
        for day_index in range(7):
            if current_day <= num_days:
                if day_index < start_day_index:
                    print("   ", end=" ")  # Print empty spaces for days before the start day
                else:
                    print(f"{current_day:2d}", end=" ")
                    current_day += 1
            else:
                print("   ", end=" ")  # Print empty spaces for days after the end of the month
        print()  # Move to the next line for the next week
