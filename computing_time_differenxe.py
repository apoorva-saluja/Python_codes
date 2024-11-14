from datetime import datetime

# Given timestamps
query_timestamp = "May 17, 2024 at 2:09 PM"
response_timestamp = "June 26, 2024 at 06:35 AM"

# Define the specific datetime format
datetime_format = '%B %d, %Y at %I:%M %p'

# Parse the datetime strings
query_datetime = datetime.strptime(query_timestamp, datetime_format)
response_datetime = datetime.strptime(response_timestamp, datetime_format)

# Calculate the difference
time_difference = response_datetime - query_datetime

# Convert the difference to hours
time_difference_in_hours = time_difference.total_seconds() / 3600

print(f"Time taken to reply: {time_difference_in_hours} hours")
