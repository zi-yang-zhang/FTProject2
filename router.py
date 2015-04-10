import util

def route(graph, dest):
	routingStack = []
	currentNode = graph[0].getNode()
	while currentNode != dest:
		routingTag = util.xor(currentNode,dest, 3)
		routingStack.append(currentNode)
		currentNode = util.getNextNode(currentNode,util.getIndexOfOne(routingTag)[0])
	routingStack.append(dest)
	return routingStack
