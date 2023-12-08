# Part 1
# Answer is .
# START TEST DATA - Answer is 4361
lines = [
"467..114..",
"...*......",
"..35..633.",
"......#...",
"617*......",
".....+.58.",
"..592.....",
"......755.",
"...$.*....",
".664.598.."]
# END TEST DATA
with open("input.txt") as f_handle:
	def clamp(value, smallest, largest): return max(smallest, min(value, largest))
	SYMBOLS = ["@", "#", "$", "%", "&", "*", "-", "+", "=", "/"]
	engine_schematic = []
	f_content = f_handle.read()
	f_content = f_content.strip()
	lines = f_content.split("\n")
	for line in lines:
		if line:
			row = []
			for col in line:
				row += [col]
			engine_schematic.append(row)
	symbol_top = False
	symbol_top_left = False
	symbol_top_right = False
	symbol_left = False
	symbol_bottom = False
	symbol_bottom_left = False
	symbol_bottom_right = False
	symbol_right = False
	potential_part_number = []
	max_row_index = len(engine_schematic) - 1
	max_col_index = len(engine_schematic[0]) - 1
	for row in engine_schematic:
		potential_part_digit = []
		for col in row:
			if col.isdigit():
				row_index = engine_schematic.index(row)
				col_index = row.index(col)
				row_top = clamp(row_index - 1, 0, row_index)
				col_left = clamp(col_index - 1, 0, col_index)
				row_bottom = clamp(row_index + 1, row_index, max_row_index)
				col_right = clamp(col_index + 1, col_index, max_col_index)
				# Check the top.
				symbol_top = True if engine_schematic[row_top][col_index] in SYMBOLS else False
				# Check the top left.
				symbol_top_left = True if engine_schematic[row_top][col_left] in SYMBOLS else False
				# Check the top right.
				symbol_top_right = True if engine_schematic[row_top][col_right] in SYMBOLS else False
				# Check the left.
				symbol_left = True if engine_schematic[row_index][col_left] in SYMBOLS else False
				# Check the bottom.
				symbol_bottom = True if engine_schematic[row_bottom][col_index] in SYMBOLS else False
				# Check the bottom left.
				symbol_bottom_left = True if engine_schematic[row_bottom][col_left] in SYMBOLS else False
				# Check the bottom right.
				symbol_bottom_right = True if engine_schematic[row_bottom][col_right] in SYMBOLS else False
				# Check the right.
				symbol_right = True if engine_schematic[row_index][col_right] in SYMBOLS else False
				#print(col, [symbol_top, symbol_top_left, symbol_top_right, symbol_left, symbol_bottom, symbol_bottom_left, symbol_bottom_right, symbol_right])
				potential_part_digit.append((col, any([symbol_top, symbol_top_left, symbol_top_right, symbol_left, symbol_bottom, symbol_bottom_left, symbol_bottom_right, symbol_right])))
			else:
				potential_part_number.append(potential_part_digit)
				potential_part_digit = []
	valid_part_numbers = []
	complete_part_number = []
	complete_is_symbol_adjacent_value = []
	for part_number in potential_part_number:
		if part_number:
			for element in part_number:
				complete_part_number.append(element[0])
				complete_is_symbol_adjacent_value.append(element[1])
			if any(complete_is_symbol_adjacent_value):
				valid_part_number = int("".join(complete_part_number))
				valid_part_numbers.append(valid_part_number)
			complete_part_number = []
			complete_is_symbol_adjacent_value = []

#print(valid_part_numbers)
print("The sum of all of the part numbers in the engine schematic for part 1 is:", sum(valid_part_numbers))