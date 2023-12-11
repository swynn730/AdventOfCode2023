# Part 1
# Answer is 26218.
# # START TEST DATA - Answer is 13
# lines = [
# "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
# "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
# "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
# "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
# "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
# "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
# ]
# # END TEST DATA
with open("input.txt") as f_handle:
	total_card_values = 0
	f_content = f_handle.read()
	f_content = f_content.strip()
	lines = f_content.split("\n")
	for line in lines:
		card_value = 0
		card, numbers = line.split(":")
		winning_numbers, your_numbers = numbers.split("|")
		winning_numbers = winning_numbers.split()
		your_numbers = your_numbers.split()
		winning_numbers_SET = set(winning_numbers)
		your_numbers_SET = set(your_numbers)
		overlapping_numbers = winning_numbers_SET.intersection(your_numbers_SET)
		overlapping_numbers_len = len(overlapping_numbers)
		if overlapping_numbers_len != 0:
			for i in range(overlapping_numbers_len):
				if i == 0:
					card_value = 1
				else:
					card_value *= 2
		total_card_values += card_value
print("The pile of cards are worth", total_card_values)


# Part 2
# Answer is .
# START TEST DATA - Answer is 30
lines = [
"Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
"Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
"Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
"Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
"Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
"Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
]
# END TEST DATA
with open("input.txt") as f_handle:
	total_card_values = 0
	f_content = f_handle.read()
	f_content = f_content.strip()
	#lines = f_content.split("\n")
	for line in lines:
		card_value = 0
		card, numbers = line.split(":")
		winning_numbers, your_numbers = numbers.split("|")
		winning_numbers = winning_numbers.split()
		your_numbers = your_numbers.split()
		winning_numbers_SET = set(winning_numbers)
		your_numbers_SET = set(your_numbers)
		overlapping_numbers = winning_numbers_SET.intersection(your_numbers_SET)
		overlapping_numbers_len = len(overlapping_numbers)
		if overlapping_numbers_len != 0:
			for i in range(overlapping_numbers_len):
				if i == 0:
					card_value = 1
				else:
					card_value *= 2
		total_card_values += card_value
print("The pile of cards are worth", total_card_values)