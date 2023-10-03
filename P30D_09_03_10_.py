##30 Days Coding Challenge
"""
Q9 -Write a program that prompts the user to enter two integers.
Suppose the integers are p and q. The program then prints p rows of q asterisks.
"""


p = int(input("Enter number of rows:"))
q = int(input("Enter number of astericks: "))

for i in range(p):
    for j in range(q):
        print("*" , end = '')
    print()
