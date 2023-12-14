# Part 1
# Answer is 275724.
# # START TEST DATA - Answer is 288
# lines = [
# "Time:      7  15   30",
# "Distance:  9  40  200",
# ]
# # END TEST DATA
with open("input.txt") as f_handle:
	ways_to_win_prod = 1
	f_content = f_handle.read()
	f_content = f_content.strip()
	lines = f_content.split("\n")
	time, distance = lines
	_, _times = time.split(":")
	_, _distances = distance.split(":")
	times = _times.split()
	distances = _distances.split()
	ways_to_win = []
	for index, (time, distance) in enumerate(zip(times, distances)):
		record_breaking_distances = []
		current_time = int(time)
		current_record = int(distance)
		for hold_time in range(current_time + 1):
			speed = current_time - hold_time
			distance_traveled = speed * hold_time
			if distance_traveled > current_record:
				record_breaking_distances.append(distance_traveled)
		ways_to_win.append(len(record_breaking_distances))
	for way_to_win in ways_to_win:
		ways_to_win_prod *= way_to_win
print("The number of ways to beat the record in each race is", ways_to_win_prod)


# Part 2
# Answer is 37286485.
# # START TEST DATA - Answer is 71503
# lines = [
# "Time:      71530",
# "Distance:  940200",
# ]
# # END TEST DATA
with open("input.txt") as f_handle:
	ways_to_win_prod = 1
	f_content = f_handle.read()
	f_content = f_content.strip()
	#lines = f_content.split("\n")
	time, distance = lines
	_, _times = time.split(":")
	_, _distances = distance.split(":")
	times = "".join(_times.split()).split()
	distances = "".join(_distances.split()).split()
	ways_to_win = []
	for index, (time, distance) in enumerate(zip(times, distances)):
		record_breaking_distances = []
		current_time = int(time)
		current_record = int(distance)
		for hold_time in range(current_time + 1):
			speed = current_time - hold_time
			distance_traveled = speed * hold_time
			if distance_traveled > current_record:
				record_breaking_distances.append(distance_traveled)
		ways_to_win.append(len(record_breaking_distances))
	for way_to_win in ways_to_win:
		ways_to_win_prod *= way_to_win
print("The number of ways to beat the record in this longer race is", ways_to_win_prod)