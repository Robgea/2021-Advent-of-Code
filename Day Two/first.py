import csv

def num_getter():
	with open("instructions.csv", encoding='utf-8') as raw_csv:
		csv_read = csv.reader(raw_csv)
		csv_list = list(csv_read)
		csv_list.pop(0)
		return_list = [row[0].split(' ') for row in csv_list]

	return return_list

def navigator(instructions):
	horiz = 0
	vert = 0

	for entry in instructions:
		if entry[0] == 'up':
			vert -= int(entry[1])
		if entry[0] == 'down':
			vert += int(entry[1])
		if entry[0] == 'forward':
			horiz += int(entry[1])

	print(f'Final results: \n \n Horiz: {horiz} \n Vert: {vert} \n \n Sum: {(horiz * vert)}')

def main():
	result = num_getter()
	navigator(result)

if __name__ == '__main__':
	main()