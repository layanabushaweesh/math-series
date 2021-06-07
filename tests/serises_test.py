# testing fibonacci function :)
from math_serises.serise import fibonacci

def test_fib_0():
 expected=0
 actual=fibonacci(0)
 assert actual == expected

def test_fib_1():
 expected=1
 actual=fibonacci(1)
 assert actual == expected

def test_fib_2():
 expected=1
 actual=fibonacci(2)
 assert actual == expected

def test_fib_3():
 expected=2
 actual=fibonacci(3)
 assert actual == expected

# testing lucas function 
from math_serises.serise import lucas

def test_luc_0():
 excepted=2
 actual=lucas(0)
 assert actual==excepted

def test_luc_1():
 excepted=1
 actual=lucas(1)
 assert actual==excepted

def test_luc_2():
 excepted=3
 actual=lucas(2)
 assert actual==excepted

def test_luc_3():
 excepted=4
 actual=lucas(3)
 assert actual==excepted

def test_luc_4():
 excepted=7
 actual=lucas(4)
 assert actual==excepted

 # testing sum function 
from math_serises.serise import sum_series

# 1- Calling this function with no optional parameters will produce numbers from the fibonacci series.
def test_sum_0():
    excepted=0
    actual=sum_series(0)
    assert actual == excepted

def test_sum_1():
    excepted=1
    actual=sum_series(1)
    assert actual == excepted 

def test_sum_2():
    excepted=1
    actual=sum_series(2)
    assert actual == excepted 

# 2- Calling it with the optional arguments 2 and 1 will produce values from the lucas.

def test_sum_lucas_0():
    excepted=2
    actual=sum_series(0,2,1)
    assert actual == excepted

def test_sum_lucas_1():
    excepted=1
    actual=sum_series(1,2,1)
    assert actual == excepted

def test_sum_lucas_2():
    excepted=3
    actual=sum_series(2,2,1)
    assert actual == excepted

# 3- Other values for the optional parameters will produce other series.

def test_sum_other_2():
    actual=sum_series(2,2,3)
    excepted=5 # i gess
    assert actual == excepted