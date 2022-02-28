def triangle_area(side_1,side_2,side_3):
    serimeter = (side_1 + side_2 + side_3) / 2
    area = (serimeter*(serimeter-side_1)*(serimeter-side_2)*(serimeter-side_3)) ** 0.5
    return area
    
print(triangle_area(12,13,14))
