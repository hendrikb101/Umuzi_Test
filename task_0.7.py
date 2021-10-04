c = int(input('Enter Celsius: '))
def temp_converter_fahrenheit(c):
    fahrenheit = (c * 9/5) + 32
    return fahrenheit
fahrenheit = temp_converter_fahrenheit(c)
print(str(fahrenheit) + " Fahrenheit")



f = int(input('Enter Fahrenheit: '))
def temp_converter_celsius(f):
    celsius = (f - 32) * 5/9
    return celsius
celsius = temp_converter_celsius(f)
print(str(celsius) + " Celsius")
