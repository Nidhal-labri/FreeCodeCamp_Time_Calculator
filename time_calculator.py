# This code was made by Nidhal LABRI #
def add_time(start, duration, day_of_week=None):
    DAYS_OF_WEEK = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
  
    # Convert start time to 24-hour format
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(":"))
    start_hour += 12 if period == "PM" and start_hour != 12 else 0
  
    # Convert duration to integers
    duration_hour, duration_minute = map(int, duration.split(":"))
  
    # Calculate total minutes
    total_minutes = start_hour * 60 + start_minute + duration_hour * 60 + duration_minute
  
    # Calculate days, hours, and minutes
    days_passed, remaining_minutes = divmod(total_minutes, 1440)
    end_hour, end_minute = divmod(remaining_minutes, 60)
  
    # Convert back to 12-hour format
    period = "PM" if end_hour >= 12 else "AM"
    end_hour = end_hour if end_hour <= 12 else end_hour - 12
    end_hour = 12 if end_hour == 0 else end_hour
  
    # Format the new time
    new_time = "{:d}:{:02d} {}".format(end_hour, end_minute, period)
  
    # If day_of_week is provided, calculate the ending day of the week
    if day_of_week:
        day_index = DAYS_OF_WEEK.index(day_of_week.capitalize())
        ending_day_index = (day_index + days_passed) % 7
        new_time += ", " + DAYS_OF_WEEK[ending_day_index]
      
    # Add day information if applicable
    if days_passed == 1:
        new_time += " (next day)"
    elif days_passed > 1:
        new_time += " ({} days later)".format(days_passed)

    return new_time