#30 Days Coding Challenge 29-09-23
"""
Q8 - Write a while loop that repeatedly prompts users to enter a number or enter “END” to exit.
After the user enters the number, the while loop simply displays the number entered. If the user enters “END”, the program displays the
message “Goodbye!” and ends.
"""

num = input("Enter a number or END to exit")
while num != 'END':
    print(num)
    num = input("Enter a number or END to exit: ")
    
print('GoodBye!')
