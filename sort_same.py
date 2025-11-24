import pandas as pd

name = input("Enter location name: ")

# Load the provided Excel file
file_path = name + '.xlsx'
df = pd.read_excel(file_path, sheet_name='Sheet1')

# Sort columns alphabetically by names
sorted_df = df.reindex(sorted(df.columns), axis=1)

# Save to a new Excel file
output_file_path = name +'.xlsx'
sorted_df.to_excel(output_file_path, index=False)
print(f"Sorted columns and saved to {output_file_path}")