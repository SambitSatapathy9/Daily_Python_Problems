#30 Days Coding Challenge 30-09-23
#Q6 - List comprehension
l = [5,12,10,14,52,36,4,2,6,97]

list1 = []
for i in l:
    if i%2 == 0:
        list1.append(i)
print("The final list using a for loop:",list1)

#USING LIST COMPREHENSION
list1 = [i for i in l if i%2 == 0]
list1
