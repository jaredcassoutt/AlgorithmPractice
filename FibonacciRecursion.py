'''
     --- Directions
     Print out the n-th entry in the fibonacci series.
     The fibonacci series is an ordering of numbers where
     each number is the sum of the preceeding two.
     For example, the sequence
      [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
     forms the first ten entries of the fibonacci series.
     
     Examples:
       FibonacciRecursion(1) === 0
       FibonacciRecursion(4) === 2
       FibonacciRecursion(20) === 4181
       
     The Memoize funtion improves upon the time complexity.
     Without Memoize, the FibonacciRecursion runs at O(2^n), 
     but with it, FibonacciRecursion runs at O(n).
    '''
def Memoize(func):
    #keeps log of data to improve run time
    cache = {}
    def checker(num):
        if num not in cache:            
            cache[num] = func(num)
        return cache[num]
    return checker
    
@Memoize
def FibonacciRecursion(n):
    #utilizes recursion to return Fibonacci number for n
    if n < 2:
        return n
    return FibonacciRecursion(n-1) + FibonacciRecursion(n-2)
