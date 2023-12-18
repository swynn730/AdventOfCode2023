# Part 1
# Answer is 275724.
# START TEST DATA - Answer is 6440
lines = [
"32T3K 765",
"T55J5 684",
"KK677 28",
"KTJJT 220",
"QQQJA 483"
]
# END TEST DATA
with open("input.txt") as f_handle:
	total_winnings = 1
	card_strengths = {"A":13, "K":12, "Q":11, "J":10, "T":9, "9":8, "8":7, "7":6, "6":5, "5":4, "4":3, "3":2, "2":1}
	card_types = {1:five}
	f_content = f_handle.read()
	f_content = f_content.strip()
	lines = f_content.split("\n")
	hand_value = 0
	# Five of a kind
	highest_hand_value = 
	# Four of a king
	# Full house
	# Three of a kind
	# Two pair 
	# One pair
	# High card


	
print("The total winnings are", total_winnings)


