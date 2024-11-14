import pandas as pd

# Load the CSV files
developer_file_path = r"C:\Users\apoor\Desktop\Cradle_point-queries\csv-formatted\mobile_queries.csv"
early_access_file_path = r"C:\Users\apoor\Desktop\Cradle_point-queries\csv-formatted\network_queries.csv"

# Read the CSV files
developer_df = pd.read_csv(developer_file_path, encoding='ISO-8859-1')
early_access_df = pd.read_csv(early_access_file_path, encoding='ISO-8859-1')

# Display basic statistics to compare
print("Developer CSV - Basic Statistics:")
print(developer_df.describe(include='all'))

print("\nEarly Access CSV - Basic Statistics:")
print(early_access_df.describe(include='all'))

# Check for missing values
print("\nDeveloper CSV - Missing Values:")
print(developer_df.isnull().sum())

print("\nEarly Access CSV - Missing Values:")
print(early_access_df.isnull().sum())

# Inspect unique values in each column to find any anomalies
print("\nDeveloper CSV - Unique Values:")
print(developer_df.nunique())

print("\nEarly Access CSV - Unique Values:")
print(early_access_df.nunique())

# Display a sample of rows from both dataframes for manual comparison
print("\nDeveloper CSV - Sample Rows:")
print(developer_df.sample(5))

print("\nEarly Access CSV - Sample Rows:")
print(early_access_df.sample(5))

# Clean data: Remove extra spaces, escape quotes, and remove problematic characters if needed
developer_df = developer_df.apply(lambda col: col.str.strip().replace('"', '""') if col.dtype == "object" else col)
early_access_df = early_access_df.apply(lambda col: col.str.strip().replace('"', '""') if col.dtype == "object" else col)

# Save the cleaned developer CSV file with semicolon delimiter
cleaned_developer_file_path = r"C:\Users\apoor\Desktop\Cradle_point-queries\csv-formatted\cleaned_mobile.csv"
developer_df.to_csv(cleaned_developer_file_path, index=False, encoding='ISO-8859-1', sep=';', quoting=1)

# Save the cleaned early access CSV file with semicolon delimiter
cleaned_early_access_file_path = r"C:\Users\apoor\Desktop\Cradle_point-queries\csv-formatted\cleaned_network.csv"
early_access_df.to_csv(cleaned_early_access_file_path, index=False, encoding='ISO-8859-1', sep=';', quoting=1)

print(f"\nCleaned Developer CSV file saved to {cleaned_developer_file_path}")
print(f"\nCleaned Early Access CSV file saved to {cleaned_early_access_file_path}")
