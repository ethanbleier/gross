import csv
def read_csv(filename):
	print("***** reading data *****")
	data = []
	with open(filename, 'r') as file:
		csv_file = csv.DictReader(file)
		for row in csv_file:
			data.append(row)
		return data