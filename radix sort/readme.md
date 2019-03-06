* It is a special sorting algorithm that works only on lists of items
* It **never** makes **comparisons** between items
* It exploits the fact that information about the size of a number is encoded in the number of digits. -> if a number has 4 digits, it is larger than a number with fewer digits.
* How it works:
    * take a list of numbers (base10 lets say)
    * create a number *buckets* based on the number base you are working with (IE for base 10 you will have buckets from **0** to **9**)
    * you have to traverse the list as many times as how many digits the longest number has (for a number with 5 digits, traverse the list 5 times)
    * the first time you go through the list, look at the right-most digit of every number and place **the whole number** into its respective buckets ( IE 902 goes into the **2** bucket). Form them back into a list keeping the order in which they were placed into the buckets.
    * the second time, look at the **second right-most** digit. If there are numbers with **1 digit only**, place them into the **0** bucket as if they were **0x**
    * repeat the process as the previous 2 steps
    * at the end, the numbers should be sorted
* For this algorithm, you need some helper methods:
    * getDigit(num, place) -> return the digit in num at the given place/position value (IE **getDigit(12345, 1) returns 4**) **you start counting from right to left**
    * figure out how many digits a number has because you need to know how many times you have to place things into buckets -> **find which number has to most digis**:
        - digitCount(num) -> returns the number of digits in *num*