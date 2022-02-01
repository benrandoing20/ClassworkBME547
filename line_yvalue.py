#Function to Identify Y Coordinate Given Points that Create a Line


def get_points():
	x1 = float(input("Enter First x-Coordinate ie: 1: "))
	y1 = float(input("Enter First y-Coordinate ie: 2: "))
	x2 = float(input("Enter Second x-Coordinate ie: 3: "))
	y2 = float(input("Enter Second y-Coordinate ie: 4: "))
	x_new = float(input("Enter Third x-Coordinate ie: 5: "))
	tup1 = (x1,y1)
	tup2 = (x2,y2)
	return tup1, tup2, x_new

def find_slope(input_tuple1, input_tuple2):
	x1 = float(input_tuple1[0])
	y1 = float(input_tuple1[1])
	x2 = float(input_tuple2[0])
	y2 = float(input_tuple2[1])
	m = (y2 - y1) / (x2 - x1)
	return m

def find_y_int(slope, input_tuple2):
	m = slope
	x2 = float(input_tuple2[0])
	y2 = float(input_tuple2[1])
	y_int = y2 - m*x2
	return y_int

def find_new_y3(slope, y_int, input_x):
	m = slope
	x3 = input_x
	y3 = m * x3 + y_int
	return(y3)

def y_out(y3):
	print("The Third y-Coordinate is {:.1f}".format(y3))

if __name__ == "__main__":
	tup1, tup2, x3 = get_points()
	slope = find_slope(tup1, tup2)
	y_int = find_y_int(slope, tup2)
	y3 = find_new_y3(slope, y_int, x3)
	y_out(y3)

