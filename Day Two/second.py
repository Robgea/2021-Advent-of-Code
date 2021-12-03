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
	aim = 0
	depth = 0

	for entry in instructions:
		if entry[0] == 'up':
			aim -= int(entry[1])
		if entry[0] == 'down':
			aim += int(entry[1])
		if entry[0] == 'forward':
			horiz += int(entry[1])
			depth_change = (int(entry[1]) * aim)
			depth += depth_change

	print(f'Final results: \n \n Horiz: {horiz} \n Aim: {aim} \n \n Total: {(horiz * depth)}')

def main():
	result = num_getter()
	navigator(result)

if __name__ == '__main__':
	main()