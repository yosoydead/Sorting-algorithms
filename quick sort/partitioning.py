def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


# define the function which takes as argument an array, a start index and an ending one
#end should be the length of the input array
#in python, default arguments have to be after all normal arguments
def partition(array, end, start = 0):

    #define the pivot variable
    pivot = array[start]

    #define the variable which will be the final index position of the pivot
    swapIndex = start

    #because i chose the pivot to be the first element in the array, ill start looping
    #through the array from the second element
    for i in range(start+1, end):
        #compare the pivot
        if pivot > array[i]:
            #if an item is less than the pivot, i have to increment the swapIndex
            swapIndex+=1

            #because the current element is less than the pivot, it means that somewhere
            #along the way, there is an element at the swapIndex that is bigger than the current index
            #so we swap them
            swap(array, swapIndex, i)
    
    #at the end of the loop, i have to swap the pivot to its correct spot
    #so that it has on the left all the smaller elements and to the right 
    #all elements bigger than it
    swap(array, start, swapIndex)

    #return the index of the pivot which will be swapIndex by now
    return swapIndex

array = [4,8,2,1,5,7,6,3]

#the function returns 3 for the given index because
'''
    [4,8,2,1,5,7,6,3] -> initial state, pivot = 4, swapIndex = 0
    compare 4 and 8 -> nothing happens
    compare 4 and 2 -> 4 > 2 -> swapIndex = 1, swap 8 and 2
    [4,2,8,1,5,7,6,3]
    compare 4 and 1 -> 4 > 1 -> swapIndex = 2, swap 8 and 1
    [4,2,1,8,5,7,6,3]
    compare 4 and 5 -> nothing happens
    compare 4 and 7 -> nothing
    compare 4 and 6 -> nothing
    compare 4 and 3 -> 4 > 3 -> swapIndex = 3, swap 8(8 is at index 3 now) with 3
    [4,2,1,3,5,7,6,8]

    after the loop finishes, swap the pivot with the value at the swapIndex = 3
    [3,2,1,4,5,7,6,8]
    now, every item less than 4 are to its left and every item bigger than 4
    are to its right
'''
print(partition(array, len(array)))

        

        