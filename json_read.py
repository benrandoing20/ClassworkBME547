import json


def input_json(filename):
    in_file = open(filename, 'r') # r is for reading the JSON file
    new_variable = json.load(in_file)
    in_file.close()
    return new_variable


if __name__ == "__main__":
	filename = "patient.json"
	x = input_json(filename)
	print(x)
	print(type(x))