def isOdd( number ):
    return number % 2 == 1

def isEven( number ):
    return number % 2 == 0

inputnum = int(input("input a number"))
if(isOdd(inputnum)):
    print("odd number")

if(isEven(inputnum)):
    print("even number")