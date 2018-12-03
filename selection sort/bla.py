#this function loops through the array from a given index until
#it finds the smallest element and returns its INDEX
def findSmallest(index, array):
    #here i chose to initialize the smallest variable to be = to the index
    #parameter because from that point on i want to do the comparisons
    smallest = index

    #start the loop from the specified input index+1 to the end of the array
    #i used index+1 to do a direct comparison between the items from the initial
    #index and the next index
    for i in range(index+1, len(array)):
        #if there is going to be a value smaller than the set variable
        #rewrite it
        if array[i] < array[smallest]:
            smallest = i

    #return the index of the smallest value in the array
    return smallest

#just a simple swap function
def swap(array, index1, index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp

#note that this is a void function so it modifies the initial collection
def selection(array):
    #for each position in the array
    for i in range(0, len(array)-1):
        #find the smallest item
        smallest = findSmallest(i, array)
        #swap the current item with the smallest one and continue
        swap(array,i,smallest)

#array = [29, 10,-1,50,-25,15, 14, 37, 13,9]
array = [180, 255, 283, 136, 156, 108, 75, -29, 125,108, 155, 299, -41, 149, 129,-100, 157, -36, 277, 79, 111, 179, 253, 282, -100, 39, -40, -97, 13, -12, -94, 43]
#print(findSmallest(0,array))
selection(array)
print(array)