'''
 --- Directions
 Given a string, return the character that is most
 commonly used in the string. This character is commonly
 refered to as the mode in mathematic courses.
 --- Examples
 mode("abcccccccd") === "c"
 mode("apple 1231111") === "1"
'''
def mode(string):
    characterMap = {}
    for character in string:
        if character in characterMap.keys():
            characterMap[character] += 1
        else:
            characterMap[character] = 1
    return max(characterMap, key=characterMap.get)
        
   
