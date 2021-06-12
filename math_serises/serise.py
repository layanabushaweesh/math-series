def fibonacci(n):
    # pass
    """
    this function will return 0 if the value of n =0 
    and return 1 if n=1 
    and return the sum of previous two number in other cases
    using recursion

    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1 :
     
        return fibonacci(n-2) + fibonacci(n-1)

def lucas(n):
    # pass

    """
    this function will return 2 if the value of n =0
    and return 1 if n=1 
    and return the sum of previous two number in other cases
    using recursion

    """
  
    if n == 0:
        return 2
    if n == 1:
        return 1
    elif n > 1 :
        return lucas(n-2) + lucas(n-1)

def sum_series(n,n2=0,n3=1):

    # pass

    """
    this function will return 0 if the value of n = 0
    and return 1 if n=1 
    in other cases it will start new series from the second parameter
    and return the sum of previous two number in other cases
    using recursion

    """

    if n == 0:
        return n2
    elif n == 1:
        return n3
    else:
        return sum_series(n-1,n2,n3) + sum_series(n-2,n2,n3)