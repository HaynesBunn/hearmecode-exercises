bread_slices = 5
peanut_butter = 2
jelly = 3

if bread_slices >= 2 and peanut_butter >= 1 and jelly >= 1:
	print "I can make this many peanut butter and jelly sandwiches: {0}".format(min(bread_slices/2, peanut_butter, jelly))
elif (bread_slices >= 2 and bread_slices%2 == 1) and peanut_butter >= 1 and jelly >= 1:
	print "I can make this many peanut butter and jelly sandwiches: {0}".format()
else:
	print "I cannot make a peanut butter and jelly sandwich"
