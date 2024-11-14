import pandas as pd

# Load the cellular queries file
file_path = r'C:\Users\apoor\Desktop\CRADLEPOINT_FINAL\cellular.xlsx'  # Replace with the actual path to your file
cellular_df = pd.read_excel(file_path)

# Define expanded keyword lists for each category
keywords = {
    'Configuration Issue': ['config', 'setup', 'install', 'configure', 'settings', 'initialize', 'initialization', 'reconfigure', 'troubleshoot', 'firmware', 'update', 'upgrade', 'reset', 'boot', 'start', 'initialize', 'customize', 'adjust', 'modify', 'patch', 'reboot'],
    'User Guidance Needed': ['use', 'usage', 'how to', 'guide', 'instruction', 'tutorial', 'manual', 'help', 'support', 'explain', 'steps', 'procedure', 'walkthrough', 'details', 'learn', 'tips', 'advice', 'information', 'clarify', 'instruction', 'education', 'training'],
    'Feature Request': ['feature', 'add', 'support', 'enhancement', 'improvement', 'functionality', 'option', 'capability', 'ability', 'possibility', 'extend', 'expand', 'upgrade', 'request', 'include', 'feature request', 'feature add', 'wish list', 'future', 'roadmap'],
    'Connectivity Issue': ['connection', 'connect', 'network', 'link', 'signal', 'wifi', 'wireless', 'wired', 'internet', 'online', 'offline', 'disconnect', 'drop', 'coverage', 'bandwidth', 'latency', 'network issue', 'signal strength', 'data', 'network speed'],
    'Hardware Limitation': ['hardware', 'device', 'fail', 'failure', 'malfunction', 'breakdown', 'defect', 'issue', 'problem', 'physical', 'damage', 'repair', 'warranty', 'replacement', 'broken', 'part', 'equipment'],
    'Product Inquiry': ['price', 'buy', 'purchase', 'cost', 'expense', 'fee', 'quote', 'pricing', 'sell', 'order', 'invoice', 'billing', 'subscription', 'payment'],
    'Product Information': ['info', 'information', 'details', 'specification', 'specs', 'data', 'summary', 'description', 'feature', 'characteristics', 'overview', 'model', 'version', 'product', 'document', 'datasheet'],
}

# Define a function to categorize queries based on keyword matches
def categorize_query(query):
    query = query.lower() if isinstance(query, str) else ''
    category_scores = {category: sum(query.count(keyword) for keyword in words) for category, words in keywords.items()}
    max_score = max(category_scores.values())
    
    # Find categories with the highest score
    best_categories = [category for category, score in category_scores.items() if score == max_score and score > 0]
    
    if len(best_categories) == 1:
        return best_categories[0]
    elif len(best_categories) > 1:
        return '/'.join(best_categories)
    else:
        return 'Unknown'  # Default category if none match

# Apply the function to categorize queries
cellular_df['Category'] = cellular_df['Query'].apply(categorize_query)

# Display the first 300 queries with their categories
categorized_queries = cellular_df.head(300)

# Calculate the category counts
category_counts = categorized_queries['Category'].value_counts().reset_index()
category_counts.columns = ['Category', 'Count']

# Save the updated DataFrame and the counts to a new Excel file
output_file_path = r'C:\Users\apoor\Desktop\CRADLEPOINT_FINAL\categorized_cellular_with_categories_and_counts_v2.xlsx'  # Replace with your desired output path
with pd.ExcelWriter(output_file_path) as writer:
    categorized_queries.to_excel(writer, sheet_name='Categorized Queries', index=False)
    category_counts.to_excel(writer, sheet_name='Category Counts', index=False)

# Display the updated DataFrame with counts
print(categorized_queries[['Query', 'Category']])
print(category_counts)
