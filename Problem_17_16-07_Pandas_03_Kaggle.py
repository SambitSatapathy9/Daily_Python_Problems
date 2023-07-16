# 2. Indexing, Slicing and Assigning 
student_data = pd.read_csv("csv_student.csv",index_col = 0)
student_data

#To get a specific column in the dataframe we can use the following method
print(student_data['Age'])
#Or this too
print(student_data.Age)
#Further indexing to get specific age (here)
print(student_data['Age'][1])

df = student_data

#Index Based selection - iloc()
df.iloc[:,:]
print(f"df.iloc[0,:] - \n{df.iloc[0,:]}\n")
print(f"df.iloc[[0,1,2],:] - \n{df.iloc[[0,1,2],:]}\n")
print(f"df.iloc[:,0:3] - \n{df.iloc[:,0:3]}\n")

print(f"df.iloc[0:2,0:4] - \n{df.iloc[2:5,0:4]}\n")
print(f"df.iloc[-5:] - \n{df.iloc[-4:]} \n")

#Location Based Selection    loc()
print(f"df.loc[0,:]- \n{df.loc[0,:]}\n") #Displays row 0 and entire column 
df.loc[[0,1,2],:] #Display row with indices 0,1,2 and entire column
#Or we can use the range option
df.loc[0:2,:] #Both fetch the same result, 2nd method is usually preferred
df.loc[:,['Student','Age']] #Gives entire row and selected column
df.loc[:,'Student':'Course'] #Gives entire row and column from 1st to chosen range
df.loc[df.Age>22]
#Add more information
df.loc[df.Age>22,'Student']

""""Difference between loc() and iloc()
- iloc uses the Python stdlib indexing scheme, where the first element of the range is included and the last one excluded.
  So 0:10 will select entries 0,...,9. loc, 
- Meanwhile, indexes inclusively. So 0:10 will select entries 0,...,10"""

#CONDITIONAL SELECTION
df.Age >= 24
df.Country == 'USA' #- This operation produced a Series of True/False booleans based on the country of each record. 
# This result can then be used inside of loc to select the relevant data:
df.loc[df.Age>=24,['Student','Marks']]

#We can use the ampersand (&) to bring the two questions together: (or -> | , not -> !=)
df.loc[(df.Age>=24) & (df.Marks>80)] #and operator is used
df.loc[(df.Age>=24) | (df.Marks>80)] #or operator is used

### Pandas comes with a few built-in conditional selectors
### isin()
df.loc[df.Food.isin(['Non-Veg'])]
df.loc[df.Ratings.isin([8,9])]

### isnull()
#- The second is isnull (and its companion notnull). 
#- These methods let you highlight values which are (or are not) empty (NaN).
df.loc[df.Age.isnull()] #There are no null values in the dataframe so no output
df.loc[df.Marks.notnull()] #There are no null values thus output is whole table

#ASSIGNING DATA
#We can change the values of the entire column too 
# df.Country = "India"
# or df('Country') = "India"
# We can also use with an iterable of values
# df['Ratings'] = range(len(df),0,-1)

#3. SUMMARY FUNCTIONS AND MAPS
