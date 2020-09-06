def find_y((x1, y1), (x2, y2), x3):
    eqn = make_line((x1, y1), (x2, y2))
    y3 = find_y_3(eqn, x3)
    return y3
