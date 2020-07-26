import pandas as pd

# File location to be changed
file_path = "DedupPhoneNum.csv"


def extract_digits(input):
    return ''.join(i for i in input if i.isdigit())

'''
Original Dataframe
'''
df = pd.read_csv(file_path, dtype=str)
# df['aadhar'] = df['Aadhaar/ ID no.'].reset_index(name='co').applymap(extract_digits)
print(type(df['Aadhaar/ ID no.']))
# df['aadhar'] = extract_digits(df['Aadhaar/ ID no.'].str)
# df = df.assign(aadhar= lambda x: ''.join(i for i in x['Aadhaar/ ID no.'] if i.isdigit()))
# empty_phone_df['clean aadhar'] = pd.DataFrame.ap(df['Aadhaar/ ID no.'].values)
# print(df)



'''
Scala code for aadhar and member ID detection:
def extractDigit(ugly: String): String = {
    val filtered = ugly.filter(_.isDigit)
    
    if(filtered.size == 12) filtered else ""    
}

val temp= udf{ (c1: String, c2:String) =>
    val c1Extracted = extractDigit(c1)
    val c2Extracted = extractDigit(c2)
    if (c1Extracted == "") c2Extracted else c1Extracted
}

val mem= udf{ (c1: String, c2:String) =>
    val c1Extracted = extractDigit(c1)
    val c2Extracted = extractDigit(c2)
    if (c1Extracted == "") c2Extracted else c1Extracted
}

val dfx = df.withColumn("clean", temp(col("AadhaarID"), col("Address"), col("Parent_Guardian")))
dfx.groupBy("clean").count.sort(desc("count")).show
d2.withColumn("mem", regexp_extract($"Parent_Guardian", "[mM][dD][ -]\\d{1,4}", 0)).("mem1", substring(col("mem"), 4, 10)).show(500)

'''

