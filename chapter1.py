import math
#print("Hello World!")

def convertToCelsius(tempInFarhenheit):
    tempInCelcius = (tempInFarhenheit - 32) * 5 / 9
    return tempInCelcius
    

tempInFarhenheit = float(input())
celcius = convertToCelsius(tempInFarhenheit)
print(celcius)


def converttoFahrenheit(tempInCelcius):
    tempInFarhenheit = tempInCelcius * (9 / 5) + 32
    return tempInFarhenheit

tempInCelsius = float(input())
farhenheit = converttoFahrenheit(tempInCelsius)
print(farhenheit)