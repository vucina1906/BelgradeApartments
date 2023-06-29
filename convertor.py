#to convert it you have to use pip install openpyxl if you do not have it installed
import pandas as pd

# Read the CSV file with the correct encoding
df = pd.read_csv('data.csv', encoding='utf-8-sig')

# Save the DataFrame as an Excel file
df.to_excel('data.xlsx', index=False)