from datetime import datetime, timedelta, date

def display_current_datetime():
   
    current_date = datetime.now() # Get the current date and time
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")
    return current_date # Return for potential use in the next function

def calculate_future_date():
    
    while True:
        try:
            days_to_add_str = input("Enter the number of days to add to the current date: ")
            days_to_add = int(days_to_add_str)
            if days_to_add < 0:
                print("Please enter a non-negative number of days.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # Get today's date (or you could use the current_date from display_current_datetime
    # if you want to be precise about the time reference, but for "date" only, today() is fine)
    today = date.today() # Get just the date part of the current date

    # Calculate the future date using timedelta
    future_date = today + timedelta(days=days_to_add)

    # Format to "YYYY-MM-DD"
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

# Main execution block
if __name__ == "__main__":
    # Part 1: Display current date and time
    display_current_datetime()

    # Part 2: Calculate a future date
    calculate_future_date()