"""# Pandas: DataFrame and Series 
Pandas is a popular library for data analysis built on top of the Python programming language. Pandas generally provide two data structures for manipulating data, 
They are: 
* DataFrame
* Series
- A DataFrame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns.
- A series represents a one-dimensional array of indexed data. We can think of a Pandas series as a 1-D dataframe
"""
import pandas as pd
csvfile = "csv_song.csv" #This variable stores the path of the CSV. #Since i didn't upload the file, you can use any of your remote file. Or you can create a csv file as we will see later.
df = pd.read_csv(csvfile) #The result is stored to the variable df(dataframe)
df.head() #Now that we have the data in a data frame, we can work with it. 

#We can create a data frame out of a dictionary using DataFrame()
X = {'Student':['David','Samuel','Terry','Evan','Sam','Sum','Shaan'],'Age':[27,24,22,32,23,26,8],'Country':['UK','Canada','China','USA','India','France','Germany'],'Course':['Python','Data Structures','Machine Learning','Web Development','C++','Java','Maths'],'Marks':[85,72,89,76,90,86,78],'Ratings':[8,7,9,6,8,9,9],'Food':['Veg','Non-Veg','Non-Veg','Veg','Veg','Non-Veg','Non-Veg']}
df = pd.DataFrame(X) #Convert a dictionary to a dataframe
df.to_csv("csv_student.csv") #Save the file 

df.head(2)
df.tail(3)

# df.info() #.info() provides the essential details about your dataset, such as the number of rows and columns, the number of non-null values, what type of data is in each column, and how much memory your DataFrame is using.
df.shape  # gives (rows,columns)

df_temp = df.append(df) #Using append() will return a copy without affecting the original DataFrame. We are capturing this copy in temp so we aren't working with the real data.
df_temp.shape

df_temp = df.drop_duplicates(df) #the drop_duplicates() method will also return a copy of your DataFrame, but this time with duplicates removed.
df_temp.shape

df.columns #Gives the information of the columns in the dataframe
#Renaming the columns
df.rename(columns = {'Ratings':'Ratings_new','Grades':'Marks_new'},inplace = True)
df.columns
#------------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------------------------------------------
#------------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------------------------------------------
#------------------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------------------------------------------

#We can create a data frame out of a dictionary using DataFrame()
x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}
#casting the dictionary to a DataFrame
df = pd.DataFrame(x)
print(df)
#    We can save the new data frame using the method to_csv. The argument is the name of the csv file.
#    There are other functions to save the data frame in other formats.  df.to_excel(), etc
df.to_csv("csv_student.csv") #Make sure you include a.csv extension.

""" Exercise 2: loc() and iloc() functions


- loc() is a label based data selectiong method which means that we have to pass the name of the row or cikumn that we want to select. 
- This method includes the last element of the range passed in it.

 Syntax: loc[row_label,column_label]

"""
print(df)
df.loc[0,:] #Displays 1st row(index 0) and entire column (: indicates all)
df.loc[[0,1,2],:] #Display row with indices 0,1,2 and entire column
#Or we can use the range option
df.loc[0:2,:] #Both fetch the same result, 2nd method is usually preferred
df.loc[[0,2,4],:]
df.loc[:,['Student','Age']] #Gives entire row and selected column
df.loc[df.Age>22]
#Add more information
df.loc[df.Age>22,'Student']
"""
- iloc() is an indexed based selecting method which means that we have to pass an integer index in the method to select a specific row/column.
- This method excludes the last element of the range passed in it.
        - loc() is inclusive whereas iloc() is exclusive and it takes only integer value
        
 Syntax: iloc[row_label, column_label]
 """
print(f"df.iloc[0,:] - \n{df.iloc[0,:]}\n\ndf.iloc[[0,1,2],:] - \n{df.iloc[[0,1,2],:]}\
        \n\ndf.iloc[:,0:3] - \n{df.iloc[:,0:3]} \n\ndf.iloc[0:2,0:4] - \n{df.iloc[0:2,0:4]}")
df.iloc[0:3,2:4]






