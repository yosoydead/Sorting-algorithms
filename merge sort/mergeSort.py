import merge
#the function takes as input an array
def mergeSort(array):
    #if the array length is <= 1, return that array
    if len(array) <= 1:
        return array
    
    #define a mid point
    #this mid point helps splitting the resulting arrays in half again and again
    mid = len(array) // 2

    #to focus only on the first half, i make a recursive call from the start of
    #the array up to the mid point
    left = mergeSort(array[0:mid])

    #this does the same as the left part of the array but focuses on the right part
    right = mergeSort(array[mid:])

    #because i have two parts of an array, i have to use the merge function 
    #defined before
    return merge.merge(left,right)

array = [10,24,76,73,72,1,9]
print(mergeSort(array))