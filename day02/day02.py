# Part 1
# Answer is 2617.
# START TEST DATA - Answer is 8
# lines = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]
# END TEST DATA
with open("input.txt") as f_handle:
	NUM_RED_CUBES=12
	NUM_GREEN_CUBES=13
	NUM_BLUE_CUBES=14
	id_sum = 0
	f_content = f_handle.read()
	lines = f_content.split("\n")
	for line in lines:
		has_valid_cube_sets = []
		record = line.split(":")
		if len(record) != 2:
			continue
		header = record[0]
		body = record[1]
		_, id_num = header.split(" ")
		cube_sets = body.split(";")
		for cube_set in cube_sets:
			has_valid_num_set_red_cubes = False
			has_valid_num_set_green_cubes = False
			has_valid_num_set_blue_cubes = False
			num_set_red_cubes = 0
			num_set_green_cubes = 0
			num_set_blue_cubes = 0
			cubes = cube_set.strip().split(",")
			for cube in cubes:
				cube_num, cube_color = cube.strip().split(" ")
				if cube_color == "red":
					num_set_red_cubes = int(cube_num)
				elif cube_color == "green":
					num_set_green_cubes = int(cube_num)
				elif cube_color == "blue":
					num_set_blue_cubes = int(cube_num)
			has_valid_num_set_red_cubes = True if num_set_red_cubes <= NUM_RED_CUBES else False
			has_valid_num_set_green_cubes = True if num_set_green_cubes <= NUM_GREEN_CUBES else False
			has_valid_num_set_blue_cubes = True if num_set_blue_cubes <= NUM_BLUE_CUBES else False
			has_valid_cube_sets += [has_valid_num_set_red_cubes, has_valid_num_set_green_cubes, has_valid_num_set_blue_cubes]
		if all(has_valid_cube_sets):
			id_sum += int(id_num)
print("The sum of the IDs of the games for part 1 is:", id_sum)


# Part 2
# Answer is 59795.
# START TEST DATA - Answer is 2286
# lines = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]
# END TEST DATA
with open("input.txt") as f_handle:
	minimum_set_power_sum = 0
	f_content = f_handle.read()
	lines = f_content.split("\n")
	for line in lines:
		min_set_red_cubes = 0
		min_set_green_cubes = 0
		min_set_blue_cubes = 0
		record = line.split(":")
		if len(record) != 2:
			continue
		header = record[0]
		body = record[1]
		_, id_num = header.split(" ")
		cube_sets = body.split(";")
		for cube_set in cube_sets:
			cubes = cube_set.strip().split(",")
			for cube in cubes:
				cube_num, cube_color = cube.strip().split(" ")
				if cube_color == "red":
					min_set_red_cubes = int(cube_num) if int(cube_num) > min_set_red_cubes else min_set_red_cubes
				elif cube_color == "green":
					min_set_green_cubes = int(cube_num) if int(cube_num) > min_set_green_cubes else min_set_green_cubes
				elif cube_color == "blue":
					min_set_blue_cubes = int(cube_num) if int(cube_num) > min_set_blue_cubes else min_set_blue_cubes
		minimum_set_power_sum += (min_set_red_cubes * min_set_green_cubes * min_set_blue_cubes)
print("The sum of the power of the minimum set of cubes that must have been present for part 2 is:", minimum_set_power_sum)