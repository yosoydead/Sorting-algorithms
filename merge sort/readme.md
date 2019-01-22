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