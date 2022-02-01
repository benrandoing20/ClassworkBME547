# test_line_yvalue.py

import pytest

@pytest.mark.parametrize("input_tuple1, input_tuple2, input_x, expected",[
	[(4,9), (0,1), 2, 5],
	[(0,0), (10,20), 5, 10],
	[(-10,-10), (10,10), 0, 0],
])
def test_check_yval(input_tuple1,input_tuple2, input_x, expected):
	from line_yvalue import check_yval
	answer = check_yval(input_tuple1, input_tuple2, input_x)
	assert answer == expected