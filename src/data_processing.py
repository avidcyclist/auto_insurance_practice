import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np

def load_data(file_path):
    print("Loading data...")
    data = pd.read_excel(file_path)
    print("Data loaded successfully.")
    return data

def clean_data(df):
    print("Cleaning data...")
    # Remove duplicates
    df = df.drop_duplicates()
    # Fill missing values
    df = df.fillna(method='ffill')
    print("Data cleaned successfully.")
    return df

def transform_data(df):
    print("Transforming data...")
    # Convert categorical columns to numerical
    for col in df.select_dtypes(include=['object', 'category']).columns:
        df[col] = df[col].astype('category').cat.codes
    
    # Convert date columns to datetime
    for col in df.select_dtypes(include=['object']).columns:
        try:
            df[col] = pd.to_datetime(df[col])
        except ValueError:
            pass
    
    # Normalize numerical columns
    scaler = StandardScaler()
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
    
    print("Data transformed successfully.")
    return df

def check_missing_values(df):
    print("Checking for missing values...")
    missing_values = df.isnull().sum()
    print("Missing values checked.")
    return missing_values[missing_values > 0]

def detect_outliers(df, exclude_columns=None):
    if exclude_columns is None:
        exclude_columns = []
    
    print("Detecting outliers...")
    outliers = {}
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        if col in exclude_columns:
            continue
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        outliers[col] = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    print("Outliers detected.")
    return outliers

if __name__ == "__main__":
    file_path = 'C:\\Users\\Mitch\\Desktop\\auto-insurance-analysis\\data\\Road Accident Data.xlsx'
    
    data = load_data(file_path)
    print("Data Loaded")
    
    data = clean_data(data)
    print("Data Cleaned")
    
    data = transform_data(data)
    print("Data Transformed")
    
    missing_values = check_missing_values(data)
    print("Missing Values:\n", missing_values)
    
    # Exclude specific columns from outlier detection
    exclude_columns = ['Number_of_Casualties', 'Number_of_Vehicles']
    outliers = detect_outliers(data, exclude_columns=exclude_columns)
    print("Outliers Detected:")
    for col, outlier_df in outliers.items():
        print(f"{col}: {len(outlier_df)} outliers")