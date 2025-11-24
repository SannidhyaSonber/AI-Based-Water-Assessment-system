import pandas as pd
import numpy as np


file_name = input("Enter the Excel file name (with .xlsx extension): ")
file_path = file_name + ".xlsx"

# Load the Excel file
df_dict = pd.read_excel(file_path, sheet_name=None)

# Define unwanted values to replace with NaN
unwanted_values = ['-', 'as', '-', '-', '-', '-', '-', '-', '-',
'-', 'BDL', '3.8`','>1600','Instrument out of ', '0. 20']


'''['CL','OL','Sl.muddy','Sl.Greenis','Nil','Instrument is out of ',
'NIL','colourless','odourless',
'-', 'BDL', 'na', 'ND', 'Instrument out of order', 'Not working', 'na ', 'BDL ', 'ND ',
'C. Less','O. less','Colourless','Odourless','Instrument out of ',
'strument Disor',]
'''
# Clean each dataframe in the dictionary
for sheet, df in df_dict.items():
    # Replace unwanted exact values with NaN
    df.replace(unwanted_values, np.nan, inplace=True)
    
    # Also handle case variations and whitespace
    df = df.applymap(lambda x: np.nan if isinstance(x, str) and x.strip().lower() in [v.strip().lower() for v in unwanted_values] else x)
    
    # Update the cleaned dataframe back in the dictionary
    df_dict[sheet] = df

# Save the cleaned data back to a new Excel file
output_file_path = file_name + '.xlsx'
with pd.ExcelWriter(output_file_path) as writer:
    for sheet_name, data in df_dict.items():
        data.to_excel(writer, sheet_name=sheet_name, index=False)

print('Cleaned Excel file saved as:', output_file_path)
