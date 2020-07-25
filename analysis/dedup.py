import pandas as pd

# File location to be changed
file_path = "OriginalFile.csv"

'''
Original Dataframe
'''
df = pd.read_csv(file_path, dtype=str)

'''
Non empty phone no. df - empty_phone_df
'''
empty_phone_df = df[df['Phone no.'].isna()]
empty_phone_df = empty_phone_df.assign(count= "1.0")

phone_count_df = df.groupby('Phone no.').size().reset_index(name='count')
phone_dedup_df = df.drop_duplicates('Phone no.', keep='last')
non_empty_phone_call_count_df = pd.merge(phone_dedup_df, phone_count_df, on='Phone no.', how='outer')

# print(list(df.columns))
# print(type(phone_count_df))
# final_df['count'] = final_df['count'].astype(str)
# pd.set_option('display.max_columns', None)

merged_df = pd.concat([empty_phone_df, non_empty_phone_call_count_df])
merged_df.to_csv('DedupPhoneNum.csv')
