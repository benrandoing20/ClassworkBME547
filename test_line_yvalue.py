# test_line_yvalue.py

import pytest

@pytest.mark.parametrize("input_tuple1, input_tuple2, expected",[
	[(4,9), (0,1), 2],
	[(0,0), (10,20), 2],
	[(-10,-10), (10,10), 1],
])
def test_find_slope(input_tuple1,input_tuple2, expected):
	from line_yvalue import find_slope
	answer = find_slope(input_tuple1, input_tuple2)
	assert answer == expected

@pytest.mark.parametrize("slope, input_tuple2, expected", [
	[1, (0, 1), 1],
	[2, (10, 20), 0],
	[2, (10, 10), -10],
])
def test_find_y_int(slope, input_tuple2, expected):
	from line_yvalue import find_y_int
	answer = find_y_int(slope, input_tuple2)
	assert answer == expected