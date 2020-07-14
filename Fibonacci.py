def fibonacci(n):
    '''
     --- Directions
     Print out the n-th entry in the fibonacci series.
     The fibonacci series is an ordering of numbers where
     each number is the sum of the preceeding two.
     For example, the sequence
      [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
     forms the first ten entries of the fibonacci series.
     
     Examples:
       fibonacci(1) === 0
       fibonacci(4) === 2
       fibonacci(20) === 4181
       
     This algorithm runs in linear time and improves upon
     space complexity by only storing two digits at a time. 
    '''
    short_seq = [0,1]
    if n < 2:
        return short_seq[n-1]
    for i in range(2,n):
        holder = short_seq.pop(0)
        short_seq.append(holder+short_seq[0])
    return short_seq[1]
