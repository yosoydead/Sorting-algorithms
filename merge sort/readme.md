* The merge sort algorithms works as follows:
    1. Divide the unsorted list into _n_ sublists, each containing one element (a list of one element is considered ordered)
    2. Repeatedly **merge** sublists to produce new sorted sublists until there is only one sublist remaining. This will be the sorted list.

* The first thing I need is a _merge_ function that merges two sublists. It is useful to implement this function first. Assume the two arrays are sorted. This helper function should create a new array which is also sorted and consists of all elements in the two input arrays. **It should not modify the parameters passed to it** It should run in **O(n+m)** time and space.
* Merge function pseudocode:
    * Create an empty array
    * Look at the smallest values in each input array (which should be the first item)
    * While there are still values we haven't looked at:
        - If the value in the first array is smaller than the value in the second array, push the value from the first array int the results
        - If the value in the second array is smaller than the value in the first array, push the value from the second array int the results
        - Once we exhaust one array, push in all remaining values from the other array
* Pseudocode for the sort:
    * Break up the array into halves until you have arrays that are empty of have one element
    * Once you have smaller arrays, merge those arrays with other sorted arrays until you are back at the full length of the array
    * Once the array has been merged back together, return the merged (and sorted) array

* For an example array of [10,24,76,73,72,1,9], the process would go something like this:
    * 1. the first half of the array would be [10,24,76]
        - a) the first half of this array is [10]
        - b) the second half of this array is [24,76]
            - the first half of this array is [24]
            - the second half is [76]
            - because i have two arrays, i have to **merge** them **resulting in [24,76]**
        - c) now it is time to **merge** **a)** and **b) resulting in [10,24,76]**
    * 2. the second half of the array would be [73,72,1,9]
        - a) the first half of this array is [73,72]
            - the first half is [73]
            - the second half is [72]
            - **merge** => **[72,73]**
        - b) the second half of this array is [1,9]
            - the first half is [1]
            - the second half is [9]
            - **merge** => **[1,9]**
        - c) it is time to **merge** **a)** and **b) resulting in [1,9,72,73]**
    * 3. now it is time to **merge** the final two arrays (**1.** and **2.**) back together **resulting in [1,9,10,24,72,73,76]**