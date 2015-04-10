class Vertex(object):
	def __init__(self, node):
		self.node = node
		self.failed = False

	def __repr__(self):
		return 'node: {}, failed: {}\n'.format(self.node,self.failed)


	def getNode(self):
		return self.node

	def isFailed(self):
		return self.failed

	def setFailed(self, failed):
		self.failed = failed
