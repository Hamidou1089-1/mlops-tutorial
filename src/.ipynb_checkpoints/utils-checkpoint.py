import numpy as np
import pandas as pd



def fib(n):
    if n < 0:
        raise ValueError('Work with Positive Numbers Only')
    if n <= 1:
        return n
    a,b = 0, 1
    for _ in range(2, n+1):
        temp = b
        b = b + a
        a = temp
       
    return b
