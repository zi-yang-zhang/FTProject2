import router, util 
start, dest,dimension,faultyLinks = util.readValueFromFile("test.txt")
print "Start: " + start
print "Destination: " + dest
print "Dimension of graph: " + str(dimension)
print "Faulty links: " + str(faultyLinks)
print ""




result = router.route(start,dest, dimension,faultyLinks)

print "============================================"
print "Routes: "
for node in result:
	print node