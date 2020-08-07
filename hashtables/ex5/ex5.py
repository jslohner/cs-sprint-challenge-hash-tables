def finder(files, queries):
	file_mem = {}
	query_mem = {}
	result = []
	for f in files:
		if (f.split('/')[-1]) not in file_mem:
			file_mem[f.split('/')[-1]] = []
		file_mem[f.split('/')[-1]].append(f)
	for q in queries:
		if q in file_mem:
			result.extend(file_mem[q])
	return result

if __name__ == "__main__":
	files = [
		'/bin/foo',
		'/bin/bar',
		'/usr/bin/baz'
	]
	queries = [
		"foo",
		"qux",
		"baz"
	]
	print(finder(files, queries))
