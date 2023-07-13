#Problem 16
# Write a python program to create a class called Student with attributes name and grades (a list of integers).
#Write a method to calculate the average grade of the student.

class Student(object):
  
    def __init__(self,name,grades):
        self.name    = name
        self.grades  = grades
        
    def average(self):
        if self.grades:
            return sum(self.grades)/ len(self.grades)
        else:
            return 0
          
student = Student('Sam',[95,91,94,87,85])
average_marks = student.average()
print(f"Average grade: {average_marks}")

#Problem Statement:
""" 
Let's consider a real-life scenario where you are analyzing customer feedback for a product. You have a large dataset of customer reviews in the form of strings, and you want to extract useful information from them using the three identified tasks:
   - You want to Pre-process the customer feedback by converting all the text to lowercase.
   - After converting the text to lowercase, you want to determine the frequency of each word in the customer feedback.
   - In addition to analyzing the overall word frequencies, you want to specifically track the frequency of a particular word that is relevant to your analysis.

By performing these tasks on the customer feedback dataset, you can gain valuable insights into customer sentiment 
"""

string = "Our premium quality products are designed to enhance your performance, giving you the confidence to succeed, the confidence to excel, and the confidence to surpass your goals."
class TextAnalyzer(object):
    
    def __init__(self,text):
        formatted_txt = text.replace('.','').replace(',','').replace('?','').replace('!','')
        formatted_txt = formatted_txt.lower() #lower case conversion
        
        self.text = formatted_txt
        
    def freqAll(self):
        words = self.text.split() #converted the string into a list
        
        #Create dictionary
        freqMap = {}
        
        for word in set(words): #using set to remove the duplicates in the list
            freqMap[word] = words.count(word)
        
        return freqMap
    
    def freqOf(self,word):
        freqdict = self.freqAll() #get frequency map
        
        if word in freqdict:
            return freqdict[word]
        else:
            return 0

#Apply the above function here
#create instance
analyse = TextAnalyzer(string) 

#Call the function to convert the data into lower case
print(f"Formatted text:\n{analyse.text}") 

#Call the function to count the frequency of all the unique words
freqmap = analyse.freqAll() 
print("\nFrequency of words: \n", freqmap)

#Call the function that counts the frequency if specific word
word = 'confidence'
freq = analyse.freqOf(word)
print(f"\nThe word '{word}' appears for {freq} times")
