def top():
	print "  ______  "
	print " /      \\"
	print "/        \\"

def bottom():
	print "\\        /"
	print " \\______/"

def line():
	print "+--------+"

def hexagon():
	top()
	bottom()
	print

def teaCup():
	bottom()
	line()
	print

def stopSign():
	top()
	print "|  STOP  |"
	bottom()

def hat():
	top()
	line()

if __name__ == "__main__":
	hexagon()
	teaCup()
	stopSign()
	hat()