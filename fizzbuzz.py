'''
 --- Directions
 Write a program that console logs the numbers
 from 1 to n. But for multiples of three print
 “fizz” instead of the number and for the multiples
 of five print “buzz”. For numbers which are multiples
 of both three and five print “fizzbuzz”.
 --- Example
   fizzbuzz(5);
   1
   2
   fizz
   4
   buzz
'''

def fizzbuzz(n):
    for value in range(1,n):
        if value % 3 == 0 and value % 5 == 0:
            print('fizzbuzz')
        elif value % 3 == 0:
            print('fizz')
        elif value % 5 == 0:
            print('buzz')
        else:
            print(value)
    
