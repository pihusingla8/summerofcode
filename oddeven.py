# Method1:
def isOdd( number ):
    return number % 2 == 1

def isEven( number ):
    return number % 2 == 0

inputnum = int(input("input a number"))
if(isOdd(inputnum)):
    print("odd number")

if(isEven(inputnum)):
    print("even number")

# Method2:
num=int(input("Enter num: "))
if num%2==0:
    print("Even")
else:
    print("Odd")