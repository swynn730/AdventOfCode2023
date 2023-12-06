# Part 1
# Answer is 55108.
# START TEST DATA - Answer is 142
# lines = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
# END TEST DATA
with open("input.txt") as f_handle:
	calibration_sum = 0
	first_digit = ""
	last_digit = ""
	f_content = f_handle.read()
	lines = f_content.split("\n")
	for line in lines:
		if line:
			for char in line:
				if char.isdigit():
					first_digit = char
					break
			for char in line[::-1]:
				if char.isdigit():
					last_digit = char
					break
			calibration_sum += int(first_digit + last_digit)
print("The sum of all the calibration values for part 1 is:", calibration_sum)


# Part 2
# Answer is 56324.
# START TEST DATA - Answer is 281
# lines = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]
# END TEST DATA
import re
with open("input.txt") as f_handle:
	VALID_DIGITS = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
	calibration_sum = 0
	f_content = f_handle.read()
	lines = f_content.split("\n")
	for line in lines:
		digit_search_results = []
		first_digit = "0"
		last_digit = "0"
		if line:
			# Keep track of the indices and digits (word and number form) found in each line.
			for digit_word, digit_number in VALID_DIGITS.items():
				digit_word_search_results = re.finditer(digit_word, line)
				digit_number_search_results = re.finditer(digit_number, line)
				if digit_word_search_results:
					for digit_word_search_result in digit_word_search_results:
						digit_search_results.append((digit_word_search_result.start(), digit_word))
				if digit_number_search_results:
					for digit_number_search_result in digit_number_search_results:
						digit_search_results.append((digit_number_search_result.start(), digit_number))
			# Sort in ascending order using the indices as the sorting key.
			sorted_digit_search_results = sorted(digit_search_results, key=lambda x: x[0])
			# Look at the start.
			if sorted_digit_search_results[0][1].isdigit():
				first_digit = sorted_digit_search_results[0][1]
			else:
				first_digit = VALID_DIGITS[sorted_digit_search_results[0][1]]
			# Look at the end.
			if sorted_digit_search_results[-1][1].isdigit():
				last_digit = sorted_digit_search_results[-1][1]
			else:
				last_digit = VALID_DIGITS[sorted_digit_search_results[-1][1]]
		calibration_sum += int(first_digit + last_digit)
print("The sum of all the calibration values for part 2 is:", calibration_sum)