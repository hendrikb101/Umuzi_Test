c = int(input('Enter Celsius: '))
def temp_converter(c):
    fahrenheit = (c * 9/5) + 32
    return fahrenheit
fahrenheit = temp_converter(c)
print(str(fahrenheit) + " Fahrenheit")



f = int(input('Enter Fahrenheit: '))
def temp_converter(f):
    celsius = (f - 32) * 5/9
    return celsius
celsius = temp_converter(f)
print(str(celsius) + " Celsius")