import csv

def num_getter():
	with open("nums.csv", encoding='utf-8') as raw_csv:
		csv_read = csv.reader(raw_csv)
		csv_list = list(csv_read)
		csv_list.pop(0)
		return_list = [int(row[0]) for row in csv_list]
	return return_list

def enumerator(input_list):

	count_num = 0
	sum_total = 0
	sum_list = []

	for num in input_list:
		sum_total += num
		count_num += 1

		if count_num == 3:
			sum_list.append(sum_total)
			sum_total = 0
			count_num = 0

	enum_list = enumerate(sum_list)
	enum_dict = dict((i,v) for i,v in enum_list)

	return enum_dict

def list_maker(input_list):
	list_1 = input_list.copy()
	list_2 = input_list.copy()
	list_2.pop(0)
	list_3 = list_2.copy()
	list_3.pop(0)
	enum_1 = enumerator(list_1)
	enum_2 = enumerator(list_2)
	enum_3 = enumerator(list_3)

	result_list = []

	for key in enum_1:
		result_list.extend([enum_1[key], enum_2[key], enum_3[key]])

	return result_list


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
	enumed = list_maker(nums)
	result = looper(enumed)
	print(result)


if __name__ == '__main__':
	main()