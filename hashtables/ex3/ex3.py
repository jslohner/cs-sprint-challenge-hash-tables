def intersection(arrays):
	mem = {}
	mem2 = {}
	rtn = {}
	for i in range(len(arrays)):
		mem[i] = arrays[i]
	for key in mem:
		for num in mem[key]:
			if num in mem2:
				rtn[num] = 'intersects'
				mem2[num] += 1
			mem2[num] = 1
			# if num not in mem2:
			# 	mem2[num] = 0
			# mem2[num] += 1

	return [k for k in rtn]
	# return [k for k,v in mem2.items() if v > 1]


if __name__ == "__main__":
	arrays = []

	arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
	arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
	arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

	print(intersection(arrays))
