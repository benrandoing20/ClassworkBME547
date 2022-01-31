# test_line_yvalue.py

def import pytest

@pytest.mark.parametrize("input_tuple1, input_tuple2, input_x, expected",[
	[(0,0), (20,0), 10, 0],
	[(0,0), (0,20), 0, 10],
	[(-10,-10), (10,10),0, 0],
])
def test_check_HDL(input_tuple1,input_tuple2, input_x, expected):
	from line_valuey import identify_y
	answer = identify_y(input_tuple1, input_tuple2, input_x)
	assert answer == expected