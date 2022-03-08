def triangle_area(side_1,side_2,side_3):
    semiperimeter = (side_1 + side_2 + side_3) / 2
    area = (semiperimeter*(semiperimeter-side_1)*(semiperimeter-side_2)*(semiperimeter-side_3)) ** 0.5
    return area
    
print(triangle_area(12,13,14))
