import util
from model.Vertex import Vertex

def generate(dimension):
	graph = []
	for node in xrange(0, 2**dimension):
		graph.append(Vertex(util.toBinary(node,dimension)))

	return graph