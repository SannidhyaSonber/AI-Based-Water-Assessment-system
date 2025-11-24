import pandas as pd


file_name = input("Enter the Excel file name (with .xlsx extension): ")
file_path = file_name + ".xlsx"
unwanted_values = [ ]

# Load the excel file
excel_file = pd.ExcelFile(file_path)




def is_numeric(s,unwanted_values):
     try:
          a = float(s)  # Try converting string to a float
          #print(a,end="   ")
          return unwanted_values  # Conversion succeeded, so it is numeric
     except ValueError:
          if s not in unwanted_values:
               unwanted_values.append(s)
          print(s,end="   ")
          return unwanted_values  # Conversion failed, so it is not numeric

# Traverse all sheets column-wise and print values
for sheet_name in excel_file.sheet_names:
     df = pd.read_excel(file_path, sheet_name=sheet_name)
     print(f"\n\n\n\n\nSheet: {sheet_name}")
     for col in df.columns:
          if col == '__Sheet__' or col == 'Date' or col == 'date':
               continue
          print(f"\n\nColumn: {col}")
          for val in df[col]:
               #print(val)
               unwanted_values = is_numeric(val,unwanted_values)

print("\nUnwanted Values in the sheet are: ")
print(unwanted_values)
#   print()  # Print a blank line between sheets
