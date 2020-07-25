import pandas as pd

# File location to be changed
file_path = "DedupPhoneNum.csv"

'''
Original Dataframe
'''
df = pd.read_csv(file_path, dtype=str)
empty_phone_df = df[df['Aadhaar/ ID no.'].isna()]
print(empty_phone_df)
