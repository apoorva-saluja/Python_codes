import pandas as pd

# Load the CSV file with ISO-8859-1 encoding to handle special characters
csv_file_path = r"C:\Users\apoor\Desktop\Cradle_point-queries\csv-formatted\developer_queries.csv"
try:
    df = pd.read_csv(csv_file_path, encoding='ISO-8859-1')
    
    # Display the first few rows to verify the structure
    print("First 10 rows of the dataframe:")
    print(df.head(10))
    
    # Display the column names
    print("\nColumn names:")
    print(df.columns)
    
    # Check for extra delimiters
    for i, row in df.iterrows():
        if len(row) != 4:
            print(f"Row {i} has {len(row)} columns instead of 4: {row}")
    
    # Ensure columns are correctly named
    expected_columns = ['query', 'query_timestamp', 'response', 'response_timestamp']
    if list(df.columns) != expected_columns:
        print(f"\nUnexpected column names: {df.columns}. Expected: {expected_columns}")
        df.columns = expected_columns
    
    # Save the corrected CSV file
    corrected_csv_path = r"C:\Users\apoor\Desktop\Cradle_point-queries\csv-formatted\developer.csv"
    df.to_csv(corrected_csv_path, index=False, quoting=1)  # quoting=1 ensures quotes around all text fields
    print(f"\nCorrected CSV file saved to {corrected_csv_path}")
except Exception as e:
    print(f"Error reading the CSV file: {e}")
