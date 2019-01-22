import partitioning

#the function takes as an argument an array and two indexes which
#help the partitioning function determine where to start and stop
def qsort(array, left, right):
    #define the base case
    #as the functions keep going, at some point, left and right will have the same value
    #that is the point where the function should stop
    if left < right:
        #call the helper pivot function
        #right has to be +1 because i need the loop to go through the entire array,
        #not stop at the second to last element
        pivotIndex = partitioning.partition(array,left,right+1) #first it it will return an index of 3 for the given array

        #define the left part of the array
        #i want the function to be called on smaller and smaller arrays
        qsort(array,left,pivotIndex-1)

        #define the right part of the array
        qsort(array, pivotIndex+1, right)
    
    #return the array after everything is finished
    return array

array = [4,8,2,1,5,7,6,3]
print(qsort(array, 0, len(array)-1))