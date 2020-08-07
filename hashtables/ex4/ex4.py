def has_negatives(a):
	mem = {}
	for num in a:
		if abs(num) not in mem:
			mem[abs(num)] = 0
		mem[abs(num)] += 1

	return [k for k,v in mem.items() if v > 1]


if __name__ == "__main__":
	print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
