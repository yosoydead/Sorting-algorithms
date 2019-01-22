* The quick sort algorithm also takes advantage of the idea that an array of 0 or 1 element is already sorted.
* It works by selecting one element (called a **pivot**) and finding the index where the pivot should end up in the sorted array.
* Once the pivot is positioned appropriately, quick sort can be applied on either side of the pivot.
* Pivot helper function:
    - given an array, this helper function should designate an element as the pivot
    - it should rearrange elements in the array so that all values less than the pivot are moved to the left of the pivot and values greater than the pivot should be moved to right side of it
    - the order of elements on either side of the pivot doesn't matter
    - **this helper should do this in place; IE should not create a new array**
    - **!!!!** when completed, the helper function should return the index of the pivot
    * **Pseudocode**:
        - the selection of the pivot is important because it can have an impact on performance
        - ideally, the pivot should be chosen so that it's roughly the median value in the data set
        - the function will have **3** arguments: an array, the start index and the end index
        - store the current pivot index in a variable (it will keep track of where the pivot should end up)
        - loop through the array from the start until the end
        - if the pivot is greater than the current element, increment the pivot index variable and then swap the current element with the element at the pivot index
        - at the very end, swap the starting element with the pivot index
        - return the pivot index
* Quick sort pseudocode:
    - call the pivot helper on the array
    - when the helper returns the pivot index, recursively call the pivot helper on the subarray to the left of that index and the subarray to the right of that index
    - your base case occurs when you consider a subarray with less than 2 elements