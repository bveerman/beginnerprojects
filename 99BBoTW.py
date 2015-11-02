i = 99
while i>1:
	print str(i)+" bottles of beer on the wall"
	print str(i)+" bottles of beer"
	print "You take one down, pass it around"
	n = i-1
	if n > 1:
		print str(n)+" bottles of beer on the wall\n"
	elif n == 1:
		print str(n)+" bottle of beer on the wall\n"
	i-=1
if i == 1:
	print str(i)+" bottle of beer on the wall"
	print str(i)+" bottle of beer"
	print "You take one down, pass it around"
	print"No more bottles of beer on the wall gittest changed"