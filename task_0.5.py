x = int(input('Enter a number: '))
y = int(input('Enter a number: '))
z = int(input('Enter a number: '))
def triangle_area(x, y, z):
    total = (x + y + z) /2
    return total
total = triangle_area(x, y, z)
print(str(total) + " is the total area size of the triangle")