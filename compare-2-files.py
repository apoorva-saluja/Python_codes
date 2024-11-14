import pandas as pd

# Load the CSV files
developer_file_path = r"C:\Users\apoor\Desktop\Cradle_point-queries\csv-formatted\developer.csv"
early_access_file_path = r"C:\Users\apoor\Desktop\Cradle_point-queries\csv-formatted\early-access.csv"

# Read the CSV files
developer_df = pd.read_csv(developer_file_path, encoding='ISO-8859-1')
early_access_df = pd.read_csv(early_access_file_path, encoding='ISO-8859-1')

# Display the first few rows of each dataframe to compare
print("Developer CSV - First 5 rows:")
print(developer_df.head())

print("\nEarly Access CSV - First 5 rows:")
print(early_access_df.head())

# Display the column names to compare
developer_columns = developer_df.columns
early_access_columns = early_access_df.columns

print("\nDeveloper CSV - Columns:")
print(developer_columns)

print("\nEarly Access CSV - Columns:")
print(early_access_columns)

# Compare the columns
if list(developer_columns) == list(early_access_columns):
    print("\nThe columns in both CSV files are identical.")
else:
    print("\nThe columns in both CSV files are different.")

# Compare the data types
developer_dtypes = developer_df.dtypes
early_access_dtypes = early_access_df.dtypes

print("\nDeveloper CSV - Data Types:")
print(developer_dtypes)

print("\nEarly Access CSV - Data Types:")
print(early_access_dtypes)

# Check if data types are consistent
if developer_dtypes.equals(early_access_dtypes):
    print("\nThe data types in both CSV files are consistent.")
else:
    print("\nThe data types in both CSV files are not consistent.")
