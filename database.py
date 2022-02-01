def add_patient(patient_name, patient_id, age):
	new_patient = [patient_name, patient_id, age, []]
	return new_patient


def main():
	db = []
	x = add_patient("Ann Atlas", 342, 40)
	db.append(x)
	y = add_patient("Bob Booyles", 50, 50)
	db.append(y)
	z = add_patient("Chris Columbus", 111, 35)
	db.append(z)

	print(x)
	print(y)
	print(z)
	print(db[1])

if __name__ == "__main__":
	main()