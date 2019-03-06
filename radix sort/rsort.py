from helpers import *

def rsort(array):
    #this will be the maximum number of digits from a number
    #found in the input array
    maxDigitCount = mostDigits(array)
    #print(maxDigitCount)

    #the loop going up to the max number of digits
    for k in range(0, maxDigitCount):
        #this is going to be the array
        #holding all the buckets for every digit from 0 to 9
        digitBuckets = [
            [],#0
            [],#1
            [],#2
            [],#3
            [],#4
            [],#5
            [],#6
            [],#7
            [],#8
            [] #9
        ]

        #loop for every number in the array given
        for i in range(0, len(array)):
            #find where the current number belongs into the bucket array
            indexForBucket = getDigit(array[i], k)

            #push that number in its position into the buckets array
            digitBuckets[indexForBucket].append(array[i])


        array = concat(digitBuckets)
        print(array)

    #return the final array
    return array


array = [23,345,11, 3, 54, 5467,12,234,9852]
rsort(array)