import pytest
import find_y from y_coord

@pytest.mark.parametrize("(x1, y2), (x2, y2), x3, expected_m, expected_y3", [
    ((0, 0), (2, 2), 1, 1, 1),
    ((1, 6), (5, 8), 3, 0.5, 7),
    ((0, 10), (10, 12), 30, 1/5, 16),
    ])

def test_find_y((x1, y2), (x2, y2), x3, expected_y3){
    answer = find_y(((x1, y2), (x2, y2), x3);
    assert answer == expected_y3
}
