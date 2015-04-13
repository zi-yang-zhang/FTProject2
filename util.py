import string

def toInt(bin):
	return int(bin,2)

def toBinary(int, dimension):
	expression = '{0:0'+str(dimension)+'b}'
	return expression.format(int)

def xor(bin1,bin2, dimension):
	return toBinary(toInt(bin1)^toInt(bin2), dimension)


def getIndexOfOne(bin):
	indexes = []
	index = 0
	for i in bin:
		if(i=='1'):
			indexes.append(index)
		index = index + 1
	return indexes

def getIndexOfZero(bin):
	indexes = []
	index = 0
	for i in bin:
		if(i=='0'):
			indexes.append(index)
		index = index + 1
	return indexes


def getNextNode(currentNode, routingTag, faultyLinks, faultyNodes, routingStack):

	nodeList = list(currentNode)
	indexes = getIndexOfOne(routingTag)
	neignbors = getAllNeighbor(currentNode)
	nextNode = ''
	print "============================================"
	print "current Node: " + currentNode
	print "routing tag: " + routingTag
	#print "routing stack: " +str(routingStack)
	print "From routing tag"
	for index in indexes:
		nextNode = togglebit(nodeList, index)
		print "checking " + nextNode
		if isLinkFaulty(currentNode,nextNode,faultyLinks) or isNodeFaulty(nextNode,faultyNodes) or isTopOfRoutingStack(nextNode, routingStack) or isInRoutingStack(routingStack,nextNode):
			print "next node"
			nodeList = list(currentNode)
			continue
		else:
			print "routed to " + nextNode
			print "routing Stack: " + str(routingStack)
			print "Faulty nodes: "+ str(faultyNodes)
			print "============================================"
			return nextNode, faultyNodes, routingStack
	print "From neignbors" + str(neignbors)
	for node in neignbors:
		print "checking " + node
		if isLinkFaulty(currentNode,node,faultyLinks) or isNodeFaulty(node,faultyNodes)or isTopOfRoutingStack(node, routingStack) or isInRoutingStack(routingStack,node):
			print "next node"
			continue
		else:
			nextNode = node
			print "routed to " + nextNode
			print "routing Stack: " + str(routingStack)
			print "Faulty nodes: "+ str(faultyNodes)
			print "============================================"
			return nextNode, faultyNodes, routingStack
	print "Add "+currentNode+" to faulty node"
	faultyNodes.add(currentNode)
	#print "Faulty nodes: "+ str(faultyNodes)
	#print "From routing stack: " + str(routingStack)
	routingStack.pop()
	nextNode = routingStack.pop()
	#print "pop: " + nextNode
	#print "routing stack: " + str(routingStack)
	print "routed back to " + nextNode
	print "============================================"
	return nextNode, faultyNodes, routingStack

def isLinkFaulty(node1,node2, faultyLinks):
	for link in faultyLinks:
		if link[0]==node1:
			if link[1]==node2:
				print "link from " + node1 +" and "+ node2+ " is faulty"
				return True
		elif link[0]==node2:
			if link[1]==node1:
				print "link from " + node1 +" and "+ node2+ " is faulty"
				return True
	print "link from " + node1 +" and "+ node2+ " is not faulty"
	return False

def isNodeFaulty(node1, faultyNodes):
	for node in faultyNodes:
		if node == node1:
			print node1 +" is faulty"
			return True
	print "node " + node1 + " is not faulty"
	return False
	
def getAllNeighbor(node):
	neignbor = []
	nodeList = list(node)
	for index in xrange(len(nodeList)):
		neignbor.append(togglebit(nodeList,index))
		nodeList = list(node)
	return neignbor

def togglebit(nodeList, index):
	if nodeList[index] == '1':
		nodeList[index] = '0'
		return "".join(nodeList)
	else:
		nodeList[index] = '1'
		return "".join(nodeList)

def isInRoutingStack(routingStack,node1):
	for node in routingStack:
		if node == node1:
			print "node " + node1+ " is " + "in routing stack"
			return True
	print "node " + node1+ " is not " + "in routing stack"
	return False

def isTopOfRoutingStack(node1, routingStack):
	if routingStack == []:
		print "node " + node1 + " not at top of routing stack"
		return False
	if node1 == routingStack[-1]:
		print "node " + node1 + " at top of routing stack"
		return True
	else:
		print "node " + node1 + " not at top of routing stack"
		return False

def readValueFromFile(filePath):
    start = None
    dest = None
    dimension = None
    faultyLinks = None
    input_file = open(filePath)
    for line in input_file:
        if '#' in line:
            continue
        if start is None:
            start = line.rstrip('\n')
            continue
        if dest is None:
            dest = line.rstrip('\n')
            continue
        if dimension is None:
            dimension = line.rstrip('\n')
            continue
        if faultyLinks is None:
        	faultyLinks = generateFaultyLinks(line.rstrip('\n').split(','))
        	continue
    return start,dest,int(dimension), [] if faultyLinks is None else faultyLinks
def generateFaultyLinks(links):
	faultyLinks = []

	for link in links:
		faultyLinks.append(tuple(link.split('-')))

	return faultyLinks


	