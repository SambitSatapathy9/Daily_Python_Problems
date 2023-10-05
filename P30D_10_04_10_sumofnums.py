
"""
Write a function called sumOfTwoNumbers () that has two parameters,
target and *b .
The function checks if there exists any two numbers in b that add up to
target .
If two numbers are found, the function displays an equation showing the
addition.
If no numbers are found, the function prints the message “No result found”.
For instance, the statements below show the function being called with
different arguments.
Function Call
sumOfTwoNumbers(12, 3, 1, 4, 5, 6, 13)
Output
No result found
The function prints “No result found” for this example as it is unable to find
any two numbers from 3, 1, 4, 5, 6, 13 that add up to the target 12
"""

def sumofTwoNumbers(target, *num): #*num is used to collect any additional positional arguments into a tuple num.
    length = len(num)
    for i in range(length-1):
        for j in range(i+1, length):
            if num[i] + num[j] == target:
                print(f"{num[i]}+{num[j]} = {target}")
                return
            
    print("No records found")
    
sumofTwoNumbers(12,4,6,5,7,8,2)
sumofTwoNumbers(5,3,1,4,2)
sumofTwoNumbers(12,4,6,5,1,2)
