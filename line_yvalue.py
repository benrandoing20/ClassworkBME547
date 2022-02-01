#Function to Identify Y Coordinate Given Points that Create a Line



def check_yval(input_tuple1, input_tuple2, input_x):
	x1 = input_tuple1[0]
	y1 = input_tuple1[1]
	x2 = input_tuple2[0]
	y2 = input_tuple2[1]
	x3 = input_x
	m = (y2 - y1) / (x2 - x1)
	y_int = y2 - m*x2
	y3 = m * x3 + y_int
	return y3
