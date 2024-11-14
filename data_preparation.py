import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from textblob import TextBlob

# File paths to all uploaded sheets with your specified paths
file_paths = [
    r'C:\Users\apoor\Desktop\CRADLEPOINT_FINAL\cellular.xlsx',
    r'C:\Users\apoor\Desktop\CRADLEPOINT_FINAL\developer.xlsx',
    r'C:\Users\apoor\Desktop\CRADLEPOINT_FINAL\early-access.xlsx',
    r'C:\Users\apoor\Desktop\CRADLEPOINT_FINAL\mobile.xlsx',
    r'C:\Users\apoor\Desktop\CRADLEPOINT_FINAL\netcloud_management.xlsx',
    r'C:\Users\apoor\Desktop\CRADLEPOINT_FINAL\networking.xlsx',
    r'C:\Users\apoor\Desktop\CRADLEPOINT_FINAL\routing.xlsx',
    r'C:\Users\apoor\Desktop\CRADLEPOINT_FINAL\security.xlsx',
    r'C:\Users\apoor\Desktop\CRADLEPOINT_FINAL\wifi.xlsx'
]

# List to hold DataFrames
dfs = []

# Load each sheet and append to the list
for file_path in file_paths:
    print(f"Loading data from: {file_path}")
    df = pd.read_excel(file_path, usecols=['Query', 'Query Timestamp', 'Response', 'Response Timestamp'])
    dfs.append(df)

# Combine all DataFrames into one
combined_df = pd.concat(dfs, ignore_index=True)
print("Combined DataFrame:")
print(combined_df.head())

# Define the specific datetime format
datetime_format = '%B %d, %Y at %I:%M %p'

# Function to parse the datetime strings
def parse_datetime(date_str):
    if isinstance(date_str, str):
        try:
            return datetime.strptime(date_str, datetime_format)
        except ValueError:
            return pd.NaT
    return pd.NaT

# Apply the function to parse the datetime columns
print("Parsing 'Query Timestamp'...")
combined_df['Query Timestamp'] = combined_df['Query Timestamp'].apply(parse_datetime)
print("Parsing 'Response Timestamp'...")
combined_df['Response Timestamp'] = combined_df['Response Timestamp'].apply(parse_datetime)

# Drop rows with invalid timestamps
print("Dropping rows with invalid timestamps...")
combined_df.dropna(subset=['Query Timestamp', 'Response Timestamp'], inplace=True)
print("DataFrame after dropping invalid timestamps:")
print(combined_df.head())

# Save the cleaned and combined data for further analysis
combined_data_path = r'C:\Users\apoor\Desktop\CRADLEPOINT_FINAL\combined_data_cleaned.xlsx'
print(f"Saving cleaned data to {combined_data_path}...")
combined_df.to_excel(combined_data_path, index=False)

# Calculate response lead time in hours and days
print("Calculating response lead time in hours and days...")
combined_df['Response Lead Time (Hours)'] = (combined_df['Response Timestamp'] - combined_df['Query Timestamp']).dt.total_seconds() / 3600  # in hours

# Calculate the difference in days and hours
def calculate_time_difference(query_time, response_time):
    time_difference = response_time - query_time
    days = time_difference.days
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    return f"{days} days, {hours} hours, {minutes} minutes"

combined_df['Response Lead Time (Days and Hours)'] = combined_df.apply(lambda row: calculate_time_difference(row['Query Timestamp'], row['Response Timestamp']), axis=1)

# Calculate the average response lead time
average_response_lead_time_hours = combined_df['Response Lead Time (Hours)'].mean()
print(f'Average Response Lead Time: {average_response_lead_time_hours:.2f} hours')

# Separate responses by Cradlepoint directing to support vs. actual solutions
print("Classifying response types...")
combined_df['Response Type'] = combined_df['Response'].apply(lambda x: 'Support' if isinstance(x, str) and 'support' in x.lower() else 'Solution')

# Information Processing

# Get the most frequently asked questions
faq = Counter(combined_df['Query']).most_common(10)
faq_df = pd.DataFrame(faq, columns=['Query', 'Count'])
print("Most Frequently Asked Questions:")
print(faq_df)

# Save the FAQ data
faq_data_path = r'C:\Users\apoor\Desktop\CRADLEPOINT_FINAL\faq_data.xlsx'
print(f"Saving FAQ data to {faq_data_path}...")
faq_df.to_excel(faq_data_path, index=False)

# Check for standardized responses
response_counts = combined_df['Response'].value_counts()
standard_responses = response_counts[response_counts > 1].reset_index()
standard_responses.columns = ['Response', 'Count']
print("Standardized Responses:")
print(standard_responses)

# Save the standardized responses data
standard_responses_data_path = r'C:\Users\apoor\Desktop\CRADLEPOINT_FINAL\standard_responses_data.xlsx'
print(f"Saving standardized responses data to {standard_responses_data_path}...")
standard_responses.to_excel(standard_responses_data_path, index=False)

# Sentiment Analysis

# Perform sentiment analysis on responses
print("Performing sentiment analysis...")
combined_df['Sentiment'] = combined_df['Response'].apply(lambda x: TextBlob(x).sentiment.polarity if isinstance(x, str) else 0)
print("Sentiment Analysis Completed:")
print(combined_df[['Response', 'Sentiment']].head())

# Save the sentiment analysis data
sentiment_data_path = r'C:\Users\apoor\Desktop\CRADLEPOINT_FINAL\sentiment_analysis_data.xlsx'
print(f"Saving sentiment analysis data to {sentiment_data_path}...")
combined_df.to_excel(sentiment_data_path, index=False)

# Save the final DataFrame with response lead times
final_data_path = r'C:\Users\apoor\Desktop\CRADLEPOINT_FINAL\final_combined_data_with_lead_times.xlsx'
print(f"Saving final data with lead times to {final_data_path}...")
combined_df.to_excel(final_data_path, index=False)
