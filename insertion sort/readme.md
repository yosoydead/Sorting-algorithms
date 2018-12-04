Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list. At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there. It repeats until no input elements remain. Sorting is typically done in-place, by iterating up the array, growing the sorted list behind it.   
At each array-position, it checks the value there against the largest value in the sorted list (which happens to be next to it, in the previous array-position checked). If larger, it leaves the element in place and moves to the next. If smaller, it finds the correct position within the sorted list, shifts all the larger values up to make a space, and inserts into that correct position.  
**source https://en.wikipedia.org/wiki/Insertion_sort**

– Start with an empty left hand and cards face down on the table.

– Then remove one card at a time from the table and Insert it into the correct position in the left hand.

– To find a correct position for a card, we compare it with each of the cards already in the hand from right to left.