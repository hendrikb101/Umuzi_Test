def triangle_area(x,y,z):
    s = (x + y + z) / 2
    area = (s*(s-x)*(s-y)*(s-z)) ** 0.5
    return area
