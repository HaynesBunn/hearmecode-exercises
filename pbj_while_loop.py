bread = 10
peanut_butter = 10
jelly = 4
sandwiches = 0

while bread >= 2 and peanut_butter >= 1 and jelly >= 1:
	sandwiches = sandwiches + 1
	print "Making sandwich #{0}".format(sandwiches)
	bread = bread - 2
	peanut_butter = peanut_butter - 1
	jelly = jelly - 1
	print "I have enough bread for {0} more sandwiches, enough peanut butter for {1} more sandwiches, and enough jelly for {2} more sandwiches.".format(bread/2, peanut_butter, jelly
		)

print "All done, I made {0} sandwiches.".format(sandwiches)
	

