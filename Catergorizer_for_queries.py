import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from imblearn.pipeline import Pipeline as ImbPipeline
from imblearn.over_sampling import SMOTE
from sklearn.metrics import classification_report
from sklearn.exceptions import UndefinedMetricWarning
import warnings

# Ignore specific warning
warnings.filterwarnings("ignore", category=UndefinedMetricWarning)

# Load the fault analysis file
fault_analysis_path = r'C:\Users\apoor\Desktop\Reports\Fault_analysis.xlsx'  # Insert your path here
fault_analysis_df = pd.read_excel(fault_analysis_path, sheet_name=None)

# Load the cellular file
cellular_path = r'C:\Users\apoor\Desktop\CRADLEPOINT_FINAL\cellular.xlsx'  # Insert your path here
cellular_df = pd.read_excel(cellular_path)

# Extract relevant data from all sheets in fault analysis
fault_data = []
for sheet_name, sheet_data in fault_analysis_df.items():
    if 'QUESTION' in sheet_data.columns and 'ANSWER' in sheet_data.columns and 'TYPE OF ISSUE (CAUSE)' in sheet_data.columns:
        for i, row in sheet_data.iterrows():
            text = f"{row['QUESTION']} {row['ANSWER']}"
            label = row['TYPE OF ISSUE (CAUSE)']
            fault_data.append((text, label))

# Combine data into a single DataFrame
fault_df = pd.DataFrame(fault_data, columns=['text', 'category'])

# Remove rows with missing categories
fault_df = fault_df.dropna(subset=['category'])

# Filter categories with at least 5 samples
category_counts = fault_df['category'].value_counts()
major_categories = category_counts[category_counts >= 5].index
fault_df = fault_df[fault_df['category'].isin(major_categories)]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(fault_df['text'], fault_df['category'], test_size=0.2, random_state=42, stratify=fault_df['category'])

# Create a text processing and classification pipeline with SMOTE
model = ImbPipeline([
    ('tfidf', TfidfVectorizer()),
    ('smote', SMOTE(k_neighbors=1)),  # Reduce the number of neighbors in SMOTE
    ('clf', RandomForestClassifier())
])

# Set up hyperparameter tuning
param_grid = {
    'tfidf__max_df': [0.75, 1.0],
    'tfidf__ngram_range': [(1, 1), (1, 2)],
    'clf__n_estimators': [100, 200],
    'clf__max_depth': [None, 10, 20]
}

# Use StratifiedKFold for cross-validation
cv = StratifiedKFold(n_splits=5)

try:
    grid_search = GridSearchCV(model, param_grid, cv=cv, scoring='f1_weighted', n_jobs=1)
    grid_search.fit(X_train, y_train)

    # Best model from GridSearchCV
    best_model = grid_search.best_estimator_

    # Evaluate the best model
    y_pred = best_model.predict(X_test)
    print(classification_report(y_test, y_pred, zero_division=0))

    # Function to categorize new queries
    def categorize_new_queries(new_df):
        new_df['text'] = new_df['Query'].fillna('') + ' ' + new_df['Response'].fillna('')
        new_df['Category'] = best_model.predict(new_df['text'])
        return new_df

    # Categorize new queries
    categorized_new_queries_df = categorize_new_queries(cellular_df)

    # Save the categorized new queries to a new Excel file
    output_file_path = r'C:\Users\apoor\Desktop\CRADLEPOINT_FINAL\categorized_cellular_queries.xlsx'  # Insert your path here
    categorized_new_queries_df.to_excel(output_file_path, index=False)

    # Display the DataFrame
    print(categorized_new_queries_df.head())

except Exception as e:
    print(f"An error occurred: {e}")
