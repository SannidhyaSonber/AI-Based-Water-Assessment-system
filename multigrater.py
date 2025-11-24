import pandas as pd

# Replace these with the actual file paths of your 4 Excel files
file_paths = ['kamla_final.xlsx','west_final.xlsx', 'karbala_final.xlsx', 'yatch_final.xlsx']

# Dictionary to hold column headings for each file
column_headings = {}

# Read each file and get column headings
for i, file in enumerate(file_paths, 1):
    df = pd.read_excel(file)
    column_headings[f'File{i}'] = df.columns.tolist()

print(column_headings)

# Convert dictionary to DataFrame for saving to new Excel
columns_df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in column_headings.items()]))

print(columns_df)
# Save to new Excel file
columns_df.to_excel('column_head.xlsx', index=False)
print("Column headings saved to 'column_head.xlsx'")
