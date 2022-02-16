import logging

def analyze_data_file(filename):
    in_file = open(filename, 'r')
    keep_reading = True
    line_number = 0
    while keep_reading:
	    data_line = in_file.readline()
	    if data_line == "":
		    keep_reading = False
	    else:
		    line_number += 1
		    process_line(data_line, line_number)

    in_file.close()

def process_line(data_line, line_no):
	data_points = data_line.strip("\n").split(",")
	if len(data_points) < 5:
		logging.warning("The line {} has less than 5 data points".format(line_no))
	data_number = [float(i) for i in data_points]
	if any(i < 0 for i in data_number):
		logging.error("The line {} has a negative number".format(line_no))
		return
	if all(1.0 <= i <= 4.0 for i in data_number):
		pass
	else:
		logging.info("Line {} was out of range".format(line_no))


if __name__ == "__main__":
	logging.basicConfig(filename = "log_example", level = logging.INFO)
	analyze_data_file("logging_data.txt")