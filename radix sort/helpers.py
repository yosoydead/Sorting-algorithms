def getDigit(num, place):
    #if its the last digit you want
    #only return the modulo of 10 of the given number
    if place == 0:
        return num%10
    
    #else, find the tens or hundreds, etc to divide the given number
    #so it will have the desired last digit
    toDivide = pow(10, place)

    #divide the given number by how many thousands you want
    #floor the result so it's an int not a float
    #modulo the remainder so you get the desired digit
    result = (num//toDivide) % 10
    return result


    #example: 12345, you want the digit at index 3 that being 2
    #you have to divide 12345 by 10000 to get 12
    #after the division, modulo the remainder by 10
    #and that should be the digit you want

def digitCount(num):
    if num == 0:
        return 1
    
    count = 0
    while num != 0:
        count = count +1
        num = num // 10

    return count

print(digitCount(0))
#print(getDigit(12345, 12))