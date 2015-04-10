class Edge(object):
	def __init__(self, node1, node2,failed):
		self.node1 = node1
		self.node2 = node2
		self.failed = failed

	def __repr__(self):
		print 'node1: {}, node2: {}, failed: {}\n'.format(self.node1,self.node2,self.failed)

	def getNode(self):
		return [self.node1,self.node2]

	def isFailed(self):
		return self.failed

	def setFailed(self, failed):
		self.failed = failed
