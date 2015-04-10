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


def getNextNode(node, index):
	nodeLsit = list(node)
	nodeLsit[index] = '1'
	return "".join(nodeLsit)