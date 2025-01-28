import pandas as pd 

file_path = "employee_performance.csv"
dp = pd.read_csv(file_path)

# 1. Handle missing values in the 'Hours_Worked' column using mean imputation
if 'Hours_Worked' in dp.columns:
    hours_mean = dp['Hours_Worked'].mean()
    dp['Hours_Worked'] = dp['Hours_Worked'].fillna(hours_mean)
    
# 2. Remove duplicate rows
dp.drop_duplicates(inplace=True)

# 3.  Convert 'Date' column to datetime
if 'Date' in dp.columns:
    dp['Date'] = pd.to_datetime(dp['Date'], errors='coerce')  # Invalid dates will become NaT
    
# 4. Flag abnormally high or low 'Tasks_Per_Hour' values using the 1.5 IQR rule
if 'Tasks_Per_Hour' in dp.columns:
    Q1 = dp['Tasks_Per_Hour'].quantile(0.25)
    Q3 = dp['Tasks_Per_Hour'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR


# Add a 'Flagged' column to identify outliers
    dp['Flagged'] = ((dp['Tasks_Per_Hour'] < lower_bound) | (dp['Tasks_Per_Hour'] > upper_bound))

# Display the first few rows of the processed dataset
print (dp.head())