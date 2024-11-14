import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector


# Connect to MySQL database
conn = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='Apoorva_gmail',
    database='cradlepoint_forums'
)

# Query to aggregate data by month for all tables
query = """

SELECT 
    DATE_FORMAT(query_timestamp_dt, '%Y-%m') AS yearmonth,
    DATE_FORMAT(query_timestamp_dt, '%M') AS month_name,
    DATE_FORMAT(query_timestamp_dt, '%Y') AS year,
    QUARTER(query_timestamp_dt) AS quarter,
    'cellular' AS table_name,
    COUNT(*) AS query_count
FROM cellular
WHERE query_timestamp_dt IS NOT NULL
GROUP BY yearmonth, month_name, year, quarter

UNION ALL

SELECT 
    DATE_FORMAT(query_timestamp_dt, '%Y-%m') AS yearmonth,
    DATE_FORMAT(query_timestamp_dt, '%M') AS month_name,
    DATE_FORMAT(query_timestamp_dt, '%Y') AS year,
    QUARTER(query_timestamp_dt) AS quarter,
    'developer' AS table_name,
    COUNT(*) AS query_count
FROM developer
WHERE query_timestamp_dt IS NOT NULL
GROUP BY yearmonth, month_name, year,quarter

UNION ALL

SELECT 
    DATE_FORMAT(query_timestamp_dt, '%Y-%m') AS yearmonth,
    DATE_FORMAT(query_timestamp_dt, '%M') AS month_name,
    DATE_FORMAT(query_timestamp_dt, '%Y') AS year,
    QUARTER(query_timestamp_dt) AS quarter,
    'earlyaccess' AS table_name,
    COUNT(*) AS query_count
FROM earlyaccess
WHERE query_timestamp_dt IS NOT NULL
GROUP BY yearmonth, month_name, year,quarter


UNION ALL

SELECT 
    DATE_FORMAT(query_timestamp_dt, '%Y-%m') AS yearmonth,
    DATE_FORMAT(query_timestamp_dt, '%M') AS month_name,
    DATE_FORMAT(query_timestamp_dt, '%Y') AS year,
    QUARTER(query_timestamp_dt) AS quarter,
    'mobile' AS table_name,
    COUNT(*) AS query_count
FROM mobile
WHERE query_timestamp_dt IS NOT NULL
GROUP BY yearmonth, month_name, year,quarter

UNION ALL

SELECT 
    DATE_FORMAT(query_timestamp_dt, '%Y-%m') AS yearmonth,
    DATE_FORMAT(query_timestamp_dt, '%M') AS month_name,
    DATE_FORMAT(query_timestamp_dt, '%Y') AS year,
    QUARTER(query_timestamp_dt) AS quarter,
    'netcloudmanagement' AS table_name,
    COUNT(*) AS query_count
FROM netcloudmanagement
WHERE query_timestamp_dt IS NOT NULL
GROUP BY yearmonth, month_name, year,quarter

UNION ALL

SELECT 
    DATE_FORMAT(query_timestamp_dt, '%Y-%m') AS yearmonth,
    DATE_FORMAT(query_timestamp_dt, '%M') AS month_name,
    DATE_FORMAT(query_timestamp_dt, '%Y') AS year,
    QUARTER(query_timestamp_dt) AS quarter,
    'network' AS table_name,
    COUNT(*) AS query_count
FROM network
WHERE query_timestamp_dt IS NOT NULL
GROUP BY yearmonth, month_name, year,quarter

UNION ALL

SELECT 
    DATE_FORMAT(query_timestamp_dt, '%Y-%m') AS yearmonth,
    DATE_FORMAT(query_timestamp_dt, '%M') AS month_name,
    DATE_FORMAT(query_timestamp_dt, '%Y') AS year,
    QUARTER(query_timestamp_dt) AS quarter,
    'routing' AS table_name,
    COUNT(*) AS query_count
FROM routing
WHERE query_timestamp_dt IS NOT NULL
GROUP BY yearmonth, month_name, year,quarter 

UNION ALL

SELECT 
    DATE_FORMAT(query_timestamp_dt, '%Y-%m') AS yearmonth,
    DATE_FORMAT(query_timestamp_dt, '%M') AS month_name,
    DATE_FORMAT(query_timestamp_dt, '%Y') AS year,
    QUARTER(query_timestamp_dt) AS quarter,
    'security' AS table_name,
    COUNT(*) AS query_count
FROM security
WHERE query_timestamp_dt IS NOT NULL
GROUP BY yearmonth, month_name, year,quarter 

UNION ALL

SELECT 
    DATE_FORMAT(query_timestamp_dt, '%Y-%m') AS yearmonth,
    DATE_FORMAT(query_timestamp_dt, '%M') AS month_name,
    DATE_FORMAT(query_timestamp_dt, '%Y') AS year,
    QUARTER(query_timestamp_dt) AS quarter,
    'wifi' AS table_name,
    COUNT(*) AS query_count
FROM wifi
WHERE query_timestamp_dt IS NOT NULL
GROUP BY yearmonth, month_name, year, quarter 



ORDER BY yearmonth, table_name;

"""

# FOR EVERY MONTH
##SELECT 
##    DATE_FORMAT(query_timestamp_dt, '%Y-%m') AS yearmonth,
##    DATE_FORMAT(query_timestamp_dt, '%M') AS month_name,
##    DATE_FORMAT(query_timestamp_dt, '%Y') AS year,
##    'cellular' AS table_name,
##    COUNT(*) AS query_count
##FROM cellular
##WHERE query_timestamp_dt IS NOT NULL
##GROUP BY yearmonth, month_name, year
##
##UNION ALL
##
##SELECT 
##    DATE_FORMAT(query_timestamp_dt, '%Y-%m') AS yearmonth,
##    DATE_FORMAT(query_timestamp_dt, '%M') AS month_name,
##    DATE_FORMAT(query_timestamp_dt, '%Y') AS year,
##    'developer' AS table_name,
##    COUNT(*) AS query_count
##FROM developer
##WHERE query_timestamp_dt IS NOT NULL
##GROUP BY yearmonth, month_name, year
##
##UNION ALL
##
##SELECT 
##    DATE_FORMAT(query_timestamp_dt, '%Y-%m') AS yearmonth,
##    DATE_FORMAT(query_timestamp_dt, '%M') AS month_name,
##    DATE_FORMAT(query_timestamp_dt, '%Y') AS year,
##    'earlyaccess' AS table_name,
##    COUNT(*) AS query_count
##FROM earlyaccess
##WHERE query_timestamp_dt IS NOT NULL
##GROUP BY yearmonth, month_name, year
##
##UNION ALL
##
##SELECT 
##    DATE_FORMAT(query_timestamp_dt, '%Y-%m') AS yearmonth,
##    DATE_FORMAT(query_timestamp_dt, '%M') AS month_name,
##    DATE_FORMAT(query_timestamp_dt, '%Y') AS year,
##    'mobile' AS table_name,
##    COUNT(*) AS query_count
##FROM mobile
##WHERE query_timestamp_dt IS NOT NULL
##GROUP BY yearmonth, month_name, year
##
##UNION ALL
##
##SELECT 
##    DATE_FORMAT(query_timestamp_dt, '%Y-%m') AS yearmonth,
##    DATE_FORMAT(query_timestamp_dt, '%M') AS month_name,
##    DATE_FORMAT(query_timestamp_dt, '%Y') AS year,
##    'netcloudmanagement' AS table_name,
##    COUNT(*) AS query_count
##FROM netcloudmanagement
##WHERE query_timestamp_dt IS NOT NULL
##GROUP BY yearmonth, month_name, year
##
##UNION ALL
##
##SELECT 
##    DATE_FORMAT(query_timestamp_dt, '%Y-%m') AS yearmonth,
##    DATE_FORMAT(query_timestamp_dt, '%M') AS month_name,
##    DATE_FORMAT(query_timestamp_dt, '%Y') AS year,
##    'network' AS table_name,
##    COUNT(*) AS query_count
##FROM network
##WHERE query_timestamp_dt IS NOT NULL
##GROUP BY yearmonth, month_name, year
##
##UNION ALL
##
##SELECT 
##    DATE_FORMAT(query_timestamp_dt, '%Y-%m') AS yearmonth,
##    DATE_FORMAT(query_timestamp_dt, '%M') AS month_name,
##    DATE_FORMAT(query_timestamp_dt, '%Y') AS year,
##    'routing' AS table_name,
##    COUNT(*) AS query_count
##FROM routing
##WHERE query_timestamp_dt IS NOT NULL
##GROUP BY yearmonth, month_name, year
##
##UNION ALL
##
##SELECT 
##    DATE_FORMAT(query_timestamp_dt, '%Y-%m') AS yearmonth,
##    DATE_FORMAT(query_timestamp_dt, '%M') AS month_name,
##    DATE_FORMAT(query_timestamp_dt, '%Y') AS year,
##    'security' AS table_name,
##    COUNT(*) AS query_count
##FROM security
##WHERE query_timestamp_dt IS NOT NULL
##GROUP BY yearmonth, month_name, year
##
##UNION ALL
##
##SELECT 
##    DATE_FORMAT(query_timestamp_dt, '%Y-%m') AS yearmonth,
##    DATE_FORMAT(query_timestamp_dt, '%M') AS month_name,
##    DATE_FORMAT(query_timestamp_dt, '%Y') AS year,
##    'wifi' AS table_name,
##    COUNT(*) AS query_count
##FROM wifi
##WHERE query_timestamp_dt IS NOT NULL
##GROUP BY yearmonth, month_name, year
##
##
##
##ORDER BY yearmonth, table_name;


# for bar chart

# Load data into a pandas DataFrame
##df = pd.read_sql(query, conn)
##
### Close the connection
##conn.close()
##
### Pivot the data for easier plotting
##pivot_df = df.pivot_table(index=['yearmonth', 'month_name', 'year'], columns='table_name', values='query_count', fill_value=0)
##
### Reset the index to use it in plotting
##pivot_df = pivot_df.reset_index()
##
### Plotting the grouped bar chart
##plt.figure(figsize=(14, 8))
##
### Get the list of months and years for x-axis
##months = pivot_df['month_name'] + ' ' + pivot_df['year'].astype(str)
##
### Plot each table's data
##for table in df['table_name'].unique():
##    plt.bar(months, pivot_df[table], label=table)
##
### Formatting the plot
##plt.xlabel('Month')
##plt.ylabel('Number of Queries')
##plt.title('Monthly Query Count Across All Tables')
##plt.xticks(rotation=45)
##plt.legend(title='Table')
##plt.tight_layout()
##
### Show the plot
##plt.show()
##


# Load data into a pandas DataFrame
df = pd.read_sql(query, conn)

# Close the connection
conn.close()

# Pivot the data for easier plotting
pivot_df = df.pivot_table(index=['year', 'quarter'], columns='table_name', values='query_count', fill_value=0)

# Reset the index to use it in plotting
pivot_df = pivot_df.reset_index()

# Plotting the grouped bar chart for quarterly data
plt.figure(figsize=(14, 8))

# Get the list of quarters and years for x-axis
quarters = 'Q' + pivot_df['quarter'].astype(str) + ' ' + pivot_df['year'].astype(str)

# Plot each table's data for quarterly aggregation
for table in df['table_name'].unique():
    plt.bar(quarters, pivot_df[table], label=table)

# Formatting the plot for quarterly data
plt.xlabel('Quarter')
plt.ylabel('Number of Queries')
plt.title('Quarterly Query Count Across All Tables')
plt.xticks(rotation=45)
plt.legend(title='Table')
plt.tight_layout()
plt.show()
