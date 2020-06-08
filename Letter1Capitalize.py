'''
--- Directions
 Write a function that accepts a string.  The function should
 capitalize the first letter of each word in the string then
 return the capitalized string.
 --- Examples
   capitalize('a short sentence') --> 'A Short Sentence'
   capitalize('a lazy fox') --> 'A Lazy Fox'
   capitalize('look, it is working!') --> 'Look, It Is Working!'
'''

def capitalization(string):
    finalString = ''
    wordArr = string.split(' ')
    for item in wordArr:
        finalString += item[0].upper() + item[1:len(item)] + ' '
    finalString = finalString[:len(finalString)-1]
    return finalString
