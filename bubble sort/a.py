#a simple swap function
#takes an array and two indexes
def swap(array, index, index2):
    #a temp value will hold the first index value
    temp = array[index]

    #the first index value need to be = to the second index value
    array[index] = array[index2]

    #the second index value needs to be = to the first index value
    array[index2] = temp

#the sort function takes in just an array
def bubble(array):
    #for each item in the array do
    for i in range(0, len(array)):

        #compare the current i index value with other
        #items in the array
        #the second loop must stop at the second before last item in the array
        for j in range(0, len(array)-1):
            #if the value of j index is > than
            #the next j value, swap them
            if array[j] > array[j+1]:
                swap(array, j, j+1)

arr = [6,2,68,98,4,3,1,7,5,10,16]
print(arr)
bubble(arr)
print(arr)