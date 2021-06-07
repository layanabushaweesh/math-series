def fibonacci(n):
    # pass
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1 :
        return fibonacci(n-2) + fibonacci(n-1)

def lucas(n):
  # pass
   if n == 0:
        return 2
   if n == 1:
        return 1
   elif n > 1 :
        return lucas(n-2) + lucas(n-1)

def sum_series(n,n2=0,n3=1):
    # pass
    if n == 0:
        return n2
    elif n == 1:
        return n3
    else:
        return sum_series(n-1,n2,n3) + sum_series(n-2,n2,n3)