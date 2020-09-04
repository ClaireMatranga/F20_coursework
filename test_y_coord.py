import find_y from y_coord

def test_find_y(){
    answer = find_y((0,0), (5, 5), 3);
    expected = 3
    assert answer == expected
}
