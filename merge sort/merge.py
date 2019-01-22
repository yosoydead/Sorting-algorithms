#this will be the merging function
# merge([1,10,50], [2,14,99,100])

def merge(arr1, arr2):
#i need two indexes, one for each array to help me travers them
    i = 0
    j = 0

    #the results array
    results = []
    
    len1 = len(arr1)
    len2 = len(arr2)

    #this loop breaks once it hits the end of one of the arrays
    while i < len1 and j < len2:
        if arr1[i] < arr2[j]:
            results.append(arr1[i])
            i+=1
        # elif arr2[j] < arr1[i]:
        else:
            results.append(arr2[j])
            j+=1

    #now i just need to add the rest of the items from one of the
    #arrays to the results
    #since i dont know which one it is, ill run a while on both arrays
    while i < len1:
        results.append(arr1[i])
        i+=1
    
    while j< len2:
        results.append(arr2[j])
        j+=1

    return results



#merge([1,10,50], [2,14,99,100])
print(merge([100], [1,2,3,4,5,6]))

