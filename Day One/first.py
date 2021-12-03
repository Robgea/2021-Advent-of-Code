import csv

def num_getter():
	with open("nums.csv", encoding='utf-8') as raw_csv:
		csv_read = csv.reader(raw_csv)
		csv_list = list(csv_read)
		csv_list.pop(0)
		return_list = [int(row[0]) for row in csv_list]

	return return_list


def looper(input_list):
	first_num = 'Start'
	increase_count = 0
	
	for num in input_list:
		if first_num == 'Start':
			pass
		else:
			if num > first_num:
				increase_count += 1

		first_num = num

	return increase_count


def main():
	nums = num_getter()
	count = looper(nums)
	print(count)


if __name__ == '__main__':
	main()