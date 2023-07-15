# Pandas (Kaggle) 

import pandas as pd
#Generate Data-frame
#We use the pd.Dataframe() constructor to generate the data-frame objects
pd.DataFrame({'Yes':[50,21],'No':[131,2]})
fruits = pd.DataFrame({"Apples":[30],"Bananas":[21],'Bob':['I liked it.','It was awful'],'Sue':['Pretty good.','Bland']})
fruits

### Indexing - We can use index labels as per our wish
#### Default indexing is 0,1,2,3, and so on.
pd.DataFrame({"Apples":[30],"Bananas":[21],'Bob':['I liked it.','It was awful'],'Sue':['Pretty good.','Bland']},index = ['Product A','Product B'])

""" Series - 1D Data frame containing 1d array and an indexing column
- A Series, by contrast, is a sequence of data values. 
- If a DataFrame is a table, a Series is a list. 

And in fact you can create one with nothing more than a list:
"""
pd.Series([1,2,4,5,7,2])
#Indexing in series is similar as in dataframe
pd.Series([1,2,4,5,7,2],index = ['A','B','C','D','E','F'])

"""
## Reading data files
- Data can be stored in any of a number of different forms and formats. By far the most basic of these is the humble CSV file.
Syntax:         file  = pd.read_csv('csvfile.csv')
"""
student_data = pd.read_csv('csv_student.csv')
student_data.shape
#We can examine the contents of the resultant DataFrame using the head() command, which grabs the first five rows:
student_data.head()
"""
The pd.read_csv() function is well-endowed, with over 30 optional parameters you can specify.

To make pandas use that column for the index (instead of creating a new one from scratch), we can specify an index_col.
"""
student_data = pd.read_csv("csv_student.csv",index_col = 0)
print(student_data)
student_data = pd.read_csv("csv_student.csv",index_col = 2)
print(student_data)

# 2. Indexing, Slicing and Assigning 

