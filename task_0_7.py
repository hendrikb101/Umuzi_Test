def temp_converter_fahrenheit(c):
    fahrenheit = (c * 9/5) + 32
    return fahrenheit


def temp_converter_celsius(f):
    celsius = (f - 32) * 5/9
    return celsius

print(temp_converter_celsius(10))
print(temp_converter_fahrenheit(90))