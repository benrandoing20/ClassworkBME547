#Function to Identify Y Coordinate Given Points that Create a Line


def get_points():
	x1 = float(input("Enter First x-Coordinate ie: 1: "))
	y1 = float(input("Enter First y-Coordinate ie: 2: "))
	x2 = float(input("Enter Second x-Coordinate ie: 3: "))
	y2 = float(input("Enter Second y-Coordinate ie: 4: "))
	x_new = float(input("Enter Third x-Coordinate ie: 5: "))
	tup1 = (x1,y1)
	tup2 = (x2,y2)
	print(tup1)
	print(tup2)
	return tup1, tup2, x_new

def check_yval(input_tuple1, input_tuple2, input_x):
	x1 = float(input_tuple1[0])
	y1 = float(input_tuple1[1])
	x2 = float(input_tuple2[0])
	y2 = float(input_tuple2[1])
	x3 = float(input_x)
	m = (y2 - y1) / (x2 - x1)
	y_int = y2 - m*x2
	y3 = m * x3 + y_int
	print(y3)

if __name__ == "__main__":
	tup1, tup2, x3 = get_points()
	check_yval(tup1, tup2, x3)

