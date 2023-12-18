# Part 1
# Answer is 13019.
# # START TEST DATA - Answers are 2 and 6
# instructions = ["R", "L"]
# nodes = ["AAA", "BBB", "CCC", "DDD", "EEE", "GGG", "ZZZ"]
# node_mappings = {"AAA":("BBB", "CCC"), "BBB":("DDD", "EEE"), "CCC":("ZZZ", "GGG"), "DDD":("DDD", "DDD"), "EEE":("EEE", "EEE"), "GGG":("GGG", "GGG"), "ZZZ":("ZZZ", "ZZZ")}
# instructions = ["L", "L", "R"]
# nodes = ["AAA", "BBB", "ZZZ"]
# node_mappings = {"AAA":("BBB", "BBB"), "BBB":("AAA", "ZZZ"), "ZZZ":("ZZZ", "ZZZ")}
# # END TEST DATA
with open("input.txt") as f_handle:
	TARGET_NODE = "ZZZ"
	num_steps = 0
	f_content = f_handle.read()
	f_content = f_content.strip()
	lines = f_content.split("\n")
	# Prepping the puzzle input to work with my algorithm.
	instructions = list(lines[0])
	nodes = []
	node_mappings = {}
	for line in lines[2:]:
		node, elements = line.split("=")
		node = node.strip()
		nodes.append(node)
		elements = elements.strip()
		left_element, right_element = elements.split(",")
		left_element = left_element.strip().replace("(", "")
		right_element = right_element.strip().replace(")", "")
		node_mappings[node] = (left_element, right_element)
	# The main algorithm.
	next_node = ""
	while next_node != TARGET_NODE:
		for instruction in instructions:
			if not next_node:
				current_node = nodes[0]
			else:
				current_node = next_node
			if instruction == "L":
				next_node = node_mappings[current_node][0]
			else:
				next_node = node_mappings[current_node][1]
			num_steps += 1
			if next_node == "ZZZ":
				break	
print("The number of steps required to reach 'ZZZ' are", num_steps)


# Part 2
# Answer is .
# START TEST DATA - Answer is 6
instructions = ["L", "R"]
nodes = ["11A", "11B", "11Z", "22A", "22B", "22C", "22Z", "XXX"]
node_mappings = {"11A":("11B", "XXX"), "11B":("XXX", "11Z"), "11Z":("11B", "XXX"), "22A":("22B", "XXX"), "22B":("22C", "22C"), "22C":("22Z", "22Z"), "22Z":("22B", "22B"), "XXX":("XXX", "XXX")}
# END TEST DATA
with open("input.txt") as f_handle:
	num_steps = 0
	f_content = f_handle.read()
	f_content = f_content.strip()
	lines = f_content.split("\n")
	# Prepping the puzzle input to work with my algorithm.
	instructions = list(lines[0])
	nodes = []
	node_mappings = {}
	for line in lines[2:]:
		node, elements = line.split("=")
		node = node.strip()
		nodes.append(node)
		elements = elements.strip()
		left_element, right_element = elements.split(",")
		left_element = left_element.strip().replace("(", "")
		right_element = right_element.strip().replace(")", "")
		node_mappings[node] = (left_element, right_element)
	# The main algorithm.
	is_first_pass = True
	starting_nodes = [node for node in nodes if node.endswith("A")]
	starting_nodes_are_transformed = [False for x in range(len(starting_nodes))]
	while not all(starting_nodes_are_transformed):
		for instruction in instructions:
			for starting_node_index, starting_node in enumerate(starting_nodes):
				next_node = ""
				if starting_node.endswith("Z"):
					starting_nodes_are_transformed[starting_node_index] = True
				else:
					starting_nodes_are_transformed[starting_node_index] = False
				if instruction == "L":
					next_node = node_mappings[starting_node][0]
				else:
					next_node = node_mappings[starting_node][1]
				starting_nodes[starting_node_index] = next_node
			if is_first_pass:
				num_steps += 0
				is_first_pass = False
			else:
				num_steps += 1
			if all(starting_nodes_are_transformed):
					break
print("The number of steps required to reach all the nodes that only end with 'Z' are", num_steps)