import pandas as pd

fishermen = pd.read_csv('fishermen.csv')
vessels = pd.read_csv('Vessels2023.csv')

# Print out unique values in the relevant columns

# Extract the last name from the 'Fisherman Name' column
fishermen['Last name'] = fishermen['Fisherman Name'].str.split().str[-1].str.upper()

# Remove leading and trailing spaces from 'Owner Name'
vessels['Owner Name'] = vessels['Owner Name'].str.strip()

# Extract the last name from the 'Owner Name' column
vessels['Last name'] = vessels['Last name'].astype(str).str.upper()
vessels['ADFG Number'] = vessels['ADFG Number'].astype(str).str.upper()

# Convert 'Boat' and 'Vessel Name' to lowercase string
fishermen['Boat'] = fishermen['Boat'].astype(str).str.upper()
vessels['Vessel Name'] = vessels['Vessel Name'].astype(str).str.upper()

# Filter out NaN entries in 'Boat' column and store in a separate dataframe
fishermen_with_nan = fishermen[fishermen['Boat'].isna()]

# Drop NaN entries in 'Boat' column from the original dataframe
fishermen = fishermen.dropna(subset=['Boat'])

# Merge the two dataframes on the 'Boat', 'Vessel Name' and 'Last name' fields
merged = fishermen.merge(vessels[['ADFG Number', 'Vessel Name', 'Last name']],
                         left_on=['Boat', 'Last name'],
                         right_on=['Vessel Name', 'Last name'],
                         how='left')

# Concatenate the merged dataframe with the dataframe containing NaN entries
merged = pd.concat([merged, fishermen_with_nan])

print(merged.head())

# Export to CSV
merged.to_csv('fisherman_filtered.csv', index=False)
