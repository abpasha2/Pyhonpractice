# import pandas as pd
# d = pd.read_csv('student.csv')
# print(d.columns[:5])


# myDataset = pd.read_csv('student.csv')
# print(myDataset.columns)
# print(myDataset.describe())
# print(myDataset.memory_usage())

# Custom data frame using dictionary
# data = {'Name':['Tom', 'nick', 'krish', 'jack','Tom', 'nick', 'krish', 'jack'],
#         'Age':[20, 21, 19, 18,20, 21, 19, 18]}
# myDF = pd.DataFrame(data)
# print(myDF)

# Remove duplicate records from DataFrame
# myDF = myDF.drop_duplicates()
# print(myDF)

# dataset = pd.read_csv('student.csv')
# subset = dataset.iloc[ : , 3]
# print(subset)

# print(dataset.columns)
# print(dataset)
# rows, cols = dataset.shape
# print(cols,rows)
# a = dataset.columns.value_counts()
# print(a)
# print(dataset.dtypes) # return datatypes of each column
# dataset_req_col = dataset['name'] # return mentioned column values
# dataset_req_col = dataset[["name","gender"]] # return multiple columns values [[col1,col2...]]
# print(dataset_req_col)
# print(dataset.head(5)) # return first 5 rows if parameter is blank and number of records if parameter number is mentioned
# print(dataset.tail(10)) # return last 5 rows
# print(dataset.iloc[5:10]) # retrieve records based on passed indices

# subset = dataset.loc[(dataset["mark"] >= 80) & (dataset["gender"] == "female")] # return records based on condition
# print(subset)

# subset = dataset.loc[dataset["mark"] >= 80] [["name","mark"]] # fetched records based on condition and specific columns
# print(subset)