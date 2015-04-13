import router, util 




try:
	file_path = raw_input("Please set input file path: ")
except Exception, e:
    print e
    exit()

print 'file path: ' + file_path
start, dest,dimension,faultyLinks = util.readValueFromFile(file_path)
print "Start: " + start
print "Destination: " + dest
print "Dimension of graph: " + str(dimension)
print "Faulty links: " + str(faultyLinks)
print ""




result = router.route(start,dest, dimension,faultyLinks)

print ""
print "Routes: "
for node in result:
	print node