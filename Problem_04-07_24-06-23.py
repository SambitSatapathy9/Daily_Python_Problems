#Problem 4 (03.07.2023)
## Problem Statement - Write a Python program to count the Frequency of Words Appearing in a String Using a Dictionary

def freq(str1):
    words = [] #Create an empty list
    words = str1.split() #Break the string into a list of words
    dict1 = {} #Declare a dictionary
    for i in words:            #Use for loop to iterate the words and values to the dictionary
        dict1[i] = words.count(i)
    print (f"The frequency of words is {dict1}") #Print the dictionary

freq("Mary had a little lamb, Mary had a little lamb, Mary had a little lamb, Mary had a little lamb, Mary had a little lamb,")

#Problem 5 
## Problem Statement - Write a Python program to find common items in two lists.

color1 = "Red", "Green", "Orange", "White"
color2 = "Black", "Green", "White", "Pink"
print(set(color1) & set(color2))

#Problem 6 
## Problem Statement - Write a Python program to find total count of word little in the given string: "Mary had a little lamb Little lamb, 
##                     little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere 
##                     that Mary went The lamb was sure to go"
def countNum(string, passed_str):
    words = []
    words = string.split()
    dict = {} 
    for key in words:
        if (key = passed_str):
            dict[key] = words.count(key)
    print(f"The frequency of the word '{passed_str}' is {dict}")
text = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere  that Mary went The lamb was sure to go"
print(countNum(text,'little')

#Problem 7 
## Problem Statement - Write a Python program to generate a list of all the even numbers between 4 to 30
print(list(range(4,30,2)))


      
