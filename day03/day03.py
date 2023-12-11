# Part 1
# Answer is 521601.
# # START TEST DATA - Answer is 4361
# lines = [
# "467..114..",
# "...*......",
# "..35..633.",
# "......#...",
# "617*......",
# ".....+.58.",
# "..592.....",
# "......755.",
# "...$.*....",
# ".664.598.."
# ]
# # END TEST DATA
# # START ADDITIONAL TEST DATA (this came in CLUTCH!!!) - Answer is 702
# lines = [
# "123.234.345",
# "...*...*...",
# "..........."
# ]
# # END ADDITIONAL TEST DATA
with open("input.txt") as f_handle:
	def clamp(value, smallest, largest): return max(smallest, min(value, largest))
	SYMBOLS = ["@", "#", "$", "%", "&", "*", "-", "+", "=", "/"]
	engine_schematic = []
	f_content = f_handle.read()
	f_content = f_content.strip()
	lines = f_content.split("\n")
	for line in lines:
		row = []
		for col in line:
			row += [col]
		engine_schematic.append(row)
	symbol_top = False
	symbol_top_left = False
	symbol_left = False
	symbol_bottom_left = False
	symbol_bottom = False
	symbol_bottom_right = False
	symbol_right = False
	symbol_top_right = False
	potential_part_numbers = []
	max_row_index = len(engine_schematic) - 1
	for row_index in range(len(engine_schematic)):
		potential_part_digits = []
		max_col_index = len(engine_schematic[row_index]) - 1
		for col_index in range(len(engine_schematic[row_index])):
			if engine_schematic[row_index][col_index].isdigit():
				# For each digit in the column, check if there is a symbol around it, there are 8 directions to check.
				row_top = clamp(row_index - 1, 0, row_index)
				col_left = clamp(col_index - 1, 0, col_index)
				row_bottom = clamp(row_index + 1, row_index, max_row_index)
				col_right = clamp(col_index + 1, col_index, max_col_index)
				# Check the top.
				symbol_top = True if engine_schematic[row_top][col_index] in SYMBOLS else False
				# Check the top left.
				symbol_top_left = True if engine_schematic[row_top][col_left] in SYMBOLS else False
				# Check the left.
				symbol_left = True if engine_schematic[row_index][col_left] in SYMBOLS else False
				# Check the bottom left.
				symbol_bottom_left = True if engine_schematic[row_bottom][col_left] in SYMBOLS else False
				# Check the bottom.
				symbol_bottom = True if engine_schematic[row_bottom][col_index] in SYMBOLS else False
				# Check the bottom right.
				symbol_bottom_right = True if engine_schematic[row_bottom][col_right] in SYMBOLS else False
				# Check the right.
				symbol_right = True if engine_schematic[row_index][col_right] in SYMBOLS else False
				# Check the top right.
				symbol_top_right = True if engine_schematic[row_top][col_right] in SYMBOLS else False
				# If there is a symbol next to the digit in any direction, track it.
				potential_part_digits.append((engine_schematic[row_index][col_index], any([symbol_top, symbol_top_left, symbol_left, symbol_bottom_left, symbol_bottom, symbol_bottom_right, symbol_right, symbol_top_right])))
				# If the last column is reached, store the last series of tracked digits and restart the digit tracking.
				if col_index == max_col_index:
					potential_part_numbers.append(potential_part_digits)
					potential_part_digits = []
			else:
				# If anything besides a digit appears, store the last series of tracked digits and restart the digit tracking.
				potential_part_numbers.append(potential_part_digits)
				potential_part_digits = []
	valid_part_numbers = []
	complete_part_number = []
	complete_is_symbol_adjacent_value = []
	for part_number in potential_part_numbers:
		if part_number:
			for element in part_number:
				complete_part_number.append(element[0])
				complete_is_symbol_adjacent_value.append(element[1])
			if any(complete_is_symbol_adjacent_value):
				valid_part_numbers.append(int("".join(complete_part_number)))
			complete_part_number = []
			complete_is_symbol_adjacent_value = []
print("The sum of all of the part numbers in the engine schematic for part 1 is:", sum(valid_part_numbers))

# Part 2
# Answer is 80694070.
# # START TEST DATA - Answer is 467835
# lines = [
# "467..114..",
# "...*......",
# "..35..633.",
# "......#...",
# "617*......",
# ".....+.58.",
# "..592.....",
# "......755.",
# "...$.*....",
# ".664.598.."
# ]
# # END TEST DATA
with open("input.txt") as f_handle:
	def clamp(value, smallest, largest): return max(smallest, min(value, largest))
	SYMBOLS = ["*"]
	engine_schematic = []
	f_content = f_handle.read()
	f_content = f_content.strip()
	lines = f_content.split("\n")
	for line in lines:
		row = []
		for col in line:
			row += [col]
		engine_schematic.append(row)
	symbol_top = False
	symbol_top_left = False
	symbol_left = False
	symbol_bottom_left = False
	symbol_bottom = False
	symbol_bottom_right = False
	symbol_right = False
	symbol_top_right = False
	potential_part_numbers = []
	max_row_index = len(engine_schematic) - 1
	for row_index in range(len(engine_schematic)):
		potential_part_digits = []
		max_col_index = len(engine_schematic[row_index]) - 1
		for col_index in range(len(engine_schematic[row_index])):
			symbol_index = ()
			if engine_schematic[row_index][col_index].isdigit():
				# For each digit in the column, check if there is a symbol around it, there are 8 directions to check.
				row_top = clamp(row_index - 1, 0, row_index)
				col_left = clamp(col_index - 1, 0, col_index)
				row_bottom = clamp(row_index + 1, row_index, max_row_index)
				col_right = clamp(col_index + 1, col_index, max_col_index)
				# For the following 8 directions of each digit, also keep track of the position of the "gear" or * symbol within 
				# the engine schematic that is adjacent.
				# Check the top.
				if engine_schematic[row_top][col_index] in SYMBOLS:
					symbol_top = True
					symbol_index = (row_top, col_index)
				else:
					symbol_top = False
				# Check the top left.
				if engine_schematic[row_top][col_left] in SYMBOLS:
					symbol_top_left = True
					symbol_index = (row_top, col_left)
				else:
					symbol_top_left = False
				# Check the left.
				if engine_schematic[row_index][col_left] in SYMBOLS:
					symbol_left = True
					symbol_index = (row_index, col_left)
				else:
					symbol_left = False
				# Check the bottom left.
				if engine_schematic[row_bottom][col_left] in SYMBOLS:
					symbol_bottom_left = True 
					symbol_index = (row_bottom, col_left)
				else:
					symbol_bottom_left = False
				# Check the bottom.
				if engine_schematic[row_bottom][col_index] in SYMBOLS:
					symbol_bottom = True
					symbol_index = (row_bottom, col_index)
				else:
					symbol_bottom = False
				# Check the bottom right.
				if engine_schematic[row_bottom][col_right] in SYMBOLS:
					symbol_bottom_right = True
					symbol_index = (row_bottom, col_right)
				else:
					symbol_bottom_right = False
				# Check the right.
				if engine_schematic[row_index][col_right] in SYMBOLS:
					symbol_right = True
					symbol_index = (row_index, col_right)
				else:
					symbol_right = False
				# Check the top right.
				if engine_schematic[row_top][col_right] in SYMBOLS:
					symbol_top_right = True
					symbol_index = (row_top, col_right)
				else:
					symbol_top_right = False
				# If there is a '*' next to the digit in any direction, track it.
				potential_part_digits.append((engine_schematic[row_index][col_index], any([symbol_top, symbol_top_left, symbol_left, symbol_bottom_left, symbol_bottom, symbol_bottom_right, symbol_right, symbol_top_right]), symbol_index))
				# If the last column is reached, store the last series of tracked digits and restart the digit tracking.
				if col_index == max_col_index:
					potential_part_numbers.append(potential_part_digits)
					potential_part_digits = []
			else:
				# If anything besides a digit appears, store the last series of tracked digits and restart the digit tracking.
				potential_part_numbers.append(potential_part_digits)
				potential_part_digits = []
	complete_part_number = []
	complete_is_symbol_adjacent_value = []
	complete_gear_location = []
	gear_ratio_products = []
	gear_locations_with_part_numbers = {}
	for part_number in potential_part_numbers:
		if part_number:
			for element in part_number:
				complete_part_number.append(element[0])
				complete_is_symbol_adjacent_value.append(element[1])
				# Some digits in a part number won't be next to a gear, meaning there will be no tracked index location so ignore those empty tuples.
				if element[2]:
					complete_gear_location.append(element[2])
			if any(complete_is_symbol_adjacent_value):
				# Duplicates are irrelevant as we are ultimately looking at the whole part number and not the individual digits that make up a part number.
				complete_gear_location_NO_DUPES = list(set(complete_gear_location))
				complete_part_number_INT = int("".join(complete_part_number))
				# Populate dictionary with the locations of all the gears and the part numbers that are adjacent to them.
				if complete_gear_location_NO_DUPES[0] in gear_locations_with_part_numbers:
					gear_locations_with_part_numbers[complete_gear_location_NO_DUPES[0]] += [complete_part_number_INT]
				else:
					gear_locations_with_part_numbers[complete_gear_location_NO_DUPES[0]] = [complete_part_number_INT]
			complete_part_number = []
			complete_is_symbol_adjacent_value = []
			complete_gear_location = []
	# They keys are the unique gear locations, the values are the part numbers next to said gear. Use this dictionary setup to calculate the gear ratio
	# and then store that to be summed up later for the final answer.
	for gear_locations_with_part_numbers_key in gear_locations_with_part_numbers.keys():
		gear_locations_with_part_numbers_values = gear_locations_with_part_numbers[gear_locations_with_part_numbers_key]
		if len(gear_locations_with_part_numbers_values) == 2:
			gear_ratio = 1
			for gear_locations_with_part_numbers_value in gear_locations_with_part_numbers_values:
				gear_ratio *= gear_locations_with_part_numbers_value
			gear_ratio_products.append(gear_ratio)	
print("The sum of all the gear ratios in the engine schematic for part 2 is:", sum(gear_ratio_products))