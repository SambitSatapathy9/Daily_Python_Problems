#30 Days Coding Challenge
#Q2 - Perfect Number Challenge

def perfect_number(num):
    if num <= 1:
      return False
    div_sum = 1
    i = 2

    #Check divisors upto square root of num
    while i*i <= num:
      if num%i == 0:
        div_sum += i
        if i != num//i:
          div_sum += num//i
      i += 1

    #Check If the number is perfect
    if div_sum == num:
      print("Entered number is a perfect number")
      return True
    else:
      print("Entered number is not a perfect number")
      return False

print(perfect_number(46))
