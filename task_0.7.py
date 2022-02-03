def temp_converter_fahrenheit(c):
    fahrenheit = (c * 9/5) + 32
    print(str(fahrenheit) + " Fahrenheit")


def temp_converter_celsius(f):
    celsius = (f - 32) * 5/9
    print(str(celsius) + " Celsius")

temp_converter_celsius(120)
temp_converter_fahrenheit(30)
