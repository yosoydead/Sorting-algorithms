Given an array of N items and L = 0, Selection Sort will:
    Find the position X of the smallest item in the range of [L...N−1],
    Swap X-th item with the L-th item,
    Increase the lower-bound L by 1 and repeat Step 1 until L = N-2.
The process starts by nding the smallest value in the sequence and swaps it
with the value in the rst position of the sequence. The second smallest value
is then found and swapped with the value in the second position. This process
continues positioning each successive value by selecting them from those not yet
sorted and swapping with the values in the respective positions.