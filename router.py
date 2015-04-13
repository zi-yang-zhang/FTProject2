import util

def route(start, dest, dimension, faultyLinks):
	faultyNodes = set()
	routingStack = []
	currentNode = start
	routingStack.append(start)
	while currentNode != dest:

		routingTag = util.xor(currentNode,dest, dimension)
		
		currentNode,faultNodes,routingStack = util.getNextNode(currentNode,routingTag, faultyLinks, faultyNodes, routingStack)
		print "Add " + currentNode +" to routingStack"
		routingStack.append(currentNode)
	print "============================================"
	print ""
	print "Arrived at Destination: " + currentNode
	return routingStack
