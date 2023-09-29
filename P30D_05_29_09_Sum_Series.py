#30 Days Coding Challenge 29-09-23
#Q5 - Print the sum of series 1^3 + 2^3 + ....+ n^3 till nth term

def sum_series(n):
    sum = 0
  for i in range(n+1):
      sum += i*i*i

  return sum

n = 6
print(sum_series(6))
