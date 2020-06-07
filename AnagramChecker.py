'''
 --- Directions
 Check to see if two provided strings are anagrams of eachother.
 One string is an anagram of another if it uses the same characters
 in the same quantity. Only consider characters, not spaces
 or punctuation.  Consider capital letters to be the same as lower case
 --- Examples
   anagrams('rail safety', 'fairy tales') --> True
   anagrams('RAIL! SAFETY!', 'fairy tales') --> True
   anagrams('Hi there', 'Bye there') --> False
'''

def checkAnagran(str1,str2):
    editStr1 = sorted(''.join(e for e in str1 if e.isalnum() and e.isalpha()).lower())
    editStr2 = sorted(''.join(e for e in str2 if e.isalnum() and e.isalpha()).lower())
    return editStr1 == editStr2
