#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
	def __init__(self, source, destination):
		self.source = source
		self.destination = destination

def reconstruct_trip(tickets, length):
	mem = {}
	route = []
	for t in tickets:
		mem[t.source] = t.destination
	for i in range(length):
		if len(route) <= 0:
			route.append(mem["NONE"])
		else:
			route.append(mem[route[-1]])

	return route
