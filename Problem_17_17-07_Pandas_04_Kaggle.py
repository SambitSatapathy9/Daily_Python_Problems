#3. SUMMARY FUNCTIONS AND MAPS
#Pandas provides many simple "summary functions" (not an official name) which restructure the data in some useful way

student_data = pd.read_csv("csv_student.csv",index_col = 0)
student_data
print(student_data['Age'])
#Or this too
print(student_data.Age)
#Further indexing to get specific age (here)
print(student_data['Age'][1])

df = student_data
df.Age.describe()
"""
- This describe() method generates a high-level summary of the attributes of the given column. 
- It is type-aware, meaning that its output changes based on the data type of the input. 
- The output above only makes sense for numerical data; for string data here's what we get
"""
df.Student.describe()
df.Marks.mean()
df.Ratings.unique() #Gives out unique values of the column
df.Student.unique()
#To see a list of unique values and their frequency of occurence, 
#we can use the value_counts() method:
df.Ratings.value_counts()
df.Country.value_counts()
"""
### Maps
- A map is a term, borrowed from mathematics, for a function that takes one set of values and "maps" them to another set of values. 
- In data science we often have a need for creating new representations from existing data, or for transforming data from the format it is in now to the format that we want it to be in later.
- Maps are what handle this work, making them extremely important for getting your work done!

#### There are two mapping methods that you will use often
- map()

      The function you pass to map() should expect a single value from the Series (a point value, in the above example), and return a transformed version of that value. map() returns a new Series where all the values have been transformed by your function.

- apply()
        
       apply() is the equivalent method if we want to transform a whole DataFrame by calling a custom method on each row.
  """
df_Ratings_mean = df.Ratings.mean()
print(df.Ratings,"\nMean:" ,df_Ratings_mean)
df.Ratings.map(lambda p: p-df_Ratings_mean)

df_Marks_mean = df.Marks.mean()
df.Marks.map(lambda p: p - df_Marks_mean)
print ("Mean Marks: ", df_Marks_mean)

def Marks_mean(row):
    row.Marks = row.Marks - df_Marks_mean
    return row
"""
- Note that map() and apply() return new, transformed Series and DataFrames, respectively. They don't modify the original data they're called on.
- If we look at the first row of Ratings, we can see that it still has its original Marks value.
"""
df.Student + " - " + df.Course
df.Marks - df_Marks_mean
Markss = df.Marks.max
df.Ratings.value_counts()

# 4. Grouping and Sorting
df.groupby("Ratings").Ratings.count()
df.groupby("Ratings").Ratings.max()

df.apply(Marks_mean, axis = 'columns')
