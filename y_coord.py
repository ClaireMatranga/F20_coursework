def find_y((x1, y1), (x2, y2), x3):
    m = find_slope((x1, y1), (x2, y2))
    y3 = find_y_3((x1, x2), m, x3)
    return y3

def find_slope((x1, y1), (x2, y2)):
    m = (y2-y1)/(x2-x1)
    return m

def find_y_3((x1, y1), m, x3):
    y3 = y1 + m * (x3- x1)
    return y3
