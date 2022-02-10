def calc_square_roott(n):

	try:
		from my_calculator import sqrt
	except ModuleNotFoundError:
		from math import sqrt
		print("My_calculator module not available. Using default")

	answer = sqrt(n)
	return answer


def main():
	print(calc_square_root(4))


if __name__ == "__main__":
	main()