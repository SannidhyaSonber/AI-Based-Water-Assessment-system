import pandas as pd
import numpy as np


name = input("Enter location name: ")

# Load the Excel file
file_path = name +'_sorted.xlsx'
data = pd.read_excel(file_path, sheet_name='Sheet1')
data = data.replace(pd.NA, False).replace(float('nan'), False).fillna(False)

# Create a dictionary to hold column variables
dict_col = {}

deletion = []

# Iterate over each column and store its values in a variable named after the column
for col in data.columns:
    # Clean column name to be a valid variable name (replace spaces and special chars with underscore)
    var_name = col.strip().replace(' ', '_').replace('.', '_').replace('-', '_')
    # Store the column data in the dictionary
    dict_col[var_name] = data[col]

# Example usage: access a column variable by name
print(dict_col.keys())  # This prints all the variable names created




list_of_keys = list(dict_col.keys())
print(list_of_keys, type(list_of_keys))
if list_of_keys == list(dict_col.keys()):
    print("All keys match.")
height = len(dict_col[list_of_keys[0]])
print(len(list_of_keys))
breaker = -1





for i in range(len(list_of_keys)):
    print(breaker)
    if breaker > 0:
        breaker -= 1
        print('ByPass')
        continue
    x = list_of_keys[i]
    print(f"Values in column '{i}':{x}")
    print(dict_col[x].tolist())  # Keep NaNs to be shown
    print("\n")


    update = list(dict_col[x].tolist())
    for k in range(1 , 5):
        if (i+k) >= len(list_of_keys):
            break
        y = list_of_keys[k+i]
        if (x == y[:-2]):
            breaker += 1
            print("YES",x,y)
            for j in range(height):

                if (dict_col[y].tolist())[j] != False :
                    update[j] = (dict_col[y].tolist())[j]
                    #(dict_col[x].tolist())[j] = (dict_col[y].tolist())[j]
            
            print(y," Deleated")
            deletion.append(y)
            #del dict_col[y]
    dict_col[x] = update
    print(dict_col[x])  # Keep NaNs to be shown
    print("\n")

for i in deletion:
    del dict_col[i]
    print(f"Deleted column: {i}")



print(dict_col.keys())

#print(dict_col['Some_Column_Name'])  # Replace 'Some_Column_Name' with an actual column name from your Excel file










#Data writing in excel file
final_file = name + '_final.xlsx'
data = pd.DataFrame(dict_col)
data = data.replace(False, pd.NA)
data.to_excel(final_file, index=False)

print('Final Excel file saved as:', final_file)





