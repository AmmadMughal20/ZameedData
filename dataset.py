import pandas as pd

dataset = pd.read_csv("./Dataset/Property.csv",  on_bad_lines='skip')

ZameenData = {} # Dictionary that will store the data
values = []
for index, row in dataset.iterrows():
    values = str(row).split(";")
print(values)

# columnswithquotes = []
# plain_columns = []

# for data in dataset:
    # columnswithquotes = data.split(";")

# print("Before replacing")
# print(columns)

# for column in columnswithquotes:
    # var = column.replace('"','')
    # plain_columns.append(var)

# print("After replacing")
# print(plain_columns)

# for column in plain_columns:
#     ZameenData[column] = []

# print(ZameenData)

