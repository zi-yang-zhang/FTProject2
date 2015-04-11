import graphGenerator,router



graph = graphGenerator.generate(5)

result = router.route('10010','01101', 5)

for node in result:
	print node