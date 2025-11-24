import pandas as pd
import numpy as np
name = input("Enter location name: ")

# Load all sheets of cleaned Excel file
cleaned_file = name +'.xlsx'
df_dict = pd.read_excel(cleaned_file, sheet_name=None)

# Gather all unique column headings from all sheets
unique_columns = set()
for df in df_dict.values():
    unique_columns.update(df.columns)
unique_columns = list(unique_columns)

# Reindex each DataFrame to contain all columns, filling missing with NaN, and concatenate
all_sheets = []
for sheet, df in df_dict.items():
    df['__Sheet__'] = sheet  # Optional: Track source sheet
    all_sheets.append(df.reindex(columns=unique_columns + ['__Sheet__']))

# Concatenate all sheets into one DataFrame
result_df = pd.concat(all_sheets, ignore_index=True)

# Save the integrated DataFrame to a new Excel file
integrated_file = name + '_integrated.xlsx'
result_df.to_excel(integrated_file, index=False)

print('Integrated Excel file saved as:', integrated_file)
