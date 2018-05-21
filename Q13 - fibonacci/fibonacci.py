"""Q13

Here's another one (12th was too easy)

1. Write a recursive function to return 100th fibonacci number.
2. Optimize the function to reduce execution time. 
"""

# Going with Fibonacci: 1,2,3,5,8..
def fib(n, a=0, b=1):
  if n:
    n -= 1
    return fib(n, b, a+b) 
  else:
    return a + b

print fib(100)

