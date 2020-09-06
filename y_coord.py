def find_y (first_point, second_point, x3):
    m = find_slope(first_point, second_point)
    y3 = find_y_3(first_point, m, x3)
    return y3

def find_slope(first_point, second_point):
    m = (second_point[1]-first_point[1])/(second_point[0]-first_point[0])
    return m

def find_y_3(first_point, m, x3):
    y3 = first_point[1] + m * (x3 - first_point[0])
    return y3
