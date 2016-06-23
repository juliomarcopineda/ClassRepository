# This program converts mass measurements. Rounded to the tenth place.

def fahrenheitToCelsius(tempFahrenheit):
    celsius = (tempFahrenheit - 32) * (5.0/9.0)
    return celsius
    
def celsiusToFahrenheit(tempCelsius):
    fahrenheit = (tempCelsius * 9.0)/5.0 + 32
    return fahrenheit


if __name__ == "__main__":
    fahrenheit = 57.0
    celsius = 34.0
    
    print str(fahrenheit) + " degree F is equal to " + \
    str(round(fahrenheitToCelsius(fahrenheit),1)) + " degree C"
    print str(celsius) + " degree C is equal to " + \
    str(round(celsiusToFahrenheit(celsius),1)) + " degree F"