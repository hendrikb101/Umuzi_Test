def triangle_area(x,y,z):
    s = (x + y + z) / 2
    area = (s*(s-x)*(s-y)*(s-z)) ** 0.5
#    print(area)
    return area
    
print(triangle_area(6,5,5))


