def get_indices_of_item_weights(weights, length, limit):
	mem = {}
	for i in range(length):
		mem[weights[i]] = i

	for wkey, idx in mem.items():
		x = limit - wkey
		if x in mem:
			if wkey == x:
				return (idx, (idx - 1))
			elif idx > mem[x]:
				return (mem[wkey], mem[x])
			elif idx < mem[x]:
				return (mem[x], mem[wkey])

	return None
