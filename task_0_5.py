def triangle_area(x,y,z):
    serimeter = (x + y + z) / 2
    area = (serimeter*(serimeter-x)*(serimeter-y)*(serimeter-z)) ** 0.5
    return area
    
print(triangle_area(12,13,14))
