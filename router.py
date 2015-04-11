import util

def route(start, dest, dimension):
	routingStack = []
	currentNode = start
	while currentNode != dest:
		routingTag = util.xor(currentNode,dest, dimension)
		routingStack.append(currentNode)
		currentNode = util.getNextNode(currentNode,routingTag)
	routingStack.append(dest)
	return routingStack
