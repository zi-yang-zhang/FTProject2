import graphGenerator,router



graph = graphGenerator.generate(3)

result = router.route(graph, '011')

for node in result:
	print node