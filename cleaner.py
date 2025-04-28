import pandas as pd

# 1. Excel file ka naam lo
input_file = 'input_data.xlsx'
output_file = 'cleaned_data.xlsx'

# 2. Excel file ko read karo
df = pd.read_excel(input_file)

# 3. Duplicate rows hatao
df = df.drop_duplicates()

# 4. Empty rows hatao
df = df.dropna()

# 5. Cleaned data ko new file me save karo
df.to_excel(output_file, index=False)

print("Data cleaning complete! Cleaned file saved as 'cleaned_data.xlsx'")
