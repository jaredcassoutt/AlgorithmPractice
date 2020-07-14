'''
 --- Directions
 Given an array and chunk size, divide the array into many subarrays
 where each subarray is of length size
 --- Examples
 createChunks([1, 2, 3, 4], 2) --> [[ 1, 2], [3, 4]]
 createChunks([1, 2, 3, 4, 5], 2) --> [[ 1, 2], [3, 4], [5]]
 createChunks([1, 2, 3, 4, 5, 6, 7, 8], 3) --> [[ 1, 2, 3], [4, 5, 6], [7, 8]]
 createChunks([1, 2, 3, 4, 5], 4) --> [[ 1, 2, 3, 4], [5]]
 createChunks([1, 2, 3, 4, 5], 10) --> [[ 1, 2, 3, 4, 5]]
'''

def createChunks(chunkArray, chunkSize):
    chunks = []
    subChunk = []
    for item in chunkArray:
        subChunk.append(item)
        if len(subChunk) == chunkSize or item == chunkArray[len(chunkArray)-1]:
            chunks.append(subChunk)
            subChunk = []
    return chunks
        
