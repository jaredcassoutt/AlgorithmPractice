'''
 --- Directions
 Write a program that returns a list of all 
 primes up to a designated max.
 --- Example
   PrimeCounter(25)
   [2, 3, 5, 7, 11, 13, 17, 19, 23]
   PrimeCounter(11)
   [2, 3, 5, 7, 11]
   PrimeCounter(1)
   []
'''


def PrimeCounter(max_val):
    if max_val < 2:
        return []
    primes = [2]
    if max_val == 2:
        return primes
        
    count_start = 3
    for count in range(count_start,max_val+1):
        for checker in primes:
            if count % checker == 0:
                break
            elif checker == primes[len(primes)-1]:
                primes.append(count)
    return primes
        
    
