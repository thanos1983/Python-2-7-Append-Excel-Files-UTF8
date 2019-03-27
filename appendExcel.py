import glob
import pandas as pd

# get all files from current dir
path = './'
# file identifier with xlsx extension
file_identifier = '*.xlsx'

# append all data from xlsx files
all_data = pd.DataFrame()
for f in glob.glob(path + '/*' + file_identifier):
    df = pd.read_excel(f, encoding='utf-8')
    df.dropna(how='all', inplace=True)
    all_data = all_data.append(df, ignore_index=True)

# Temporary xlsx file to append all xlsx files
appendedXlsxFile = 'complete.xlsx'

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter(appendedXlsxFile, engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
all_data.to_excel(writer, sheet_name='Sheet1')

# Get the xlsxwriter objects from the dataframe writer object.
workbook = writer.book
worksheet = writer.sheets['Sheet1']

# Close the Pandas Excel writer and output the Excel file.
writer.save()
