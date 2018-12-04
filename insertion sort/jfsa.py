#swap function
def swap(array, index1, index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp

#sort
def insertion(array):
    #the insertion sort algorithm starts by assuming that the element at index 0
    #is already sorted, so we start with the next index
    i = 1
    
    while i < len(array):
        #for each index, we need to compare it with the previous one and see
        #if it is smaller or bigger
        j = i

        #use j>0 so the function doesnt throw index out of range
        #compare the item from the previous index with the current one
        #the loop stops either when j = 0 or the previous item is smaller than the current one
        while j > 0 and array[j-1] > array[j]:

            #if the item from the previous index is bigger than the current one
            #swap them
            swap(array, j, j-1)
            
            #decrement j so we can continue with the comparisons
            j = j-1
        
        #increment i so we dont run in an infinte loop
        i = i+1
        
array = [6,5,3,1,8,-8,4,7,2,-2]
insertion(array)
print(array)