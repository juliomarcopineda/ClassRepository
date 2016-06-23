# Julio Marco Pineda
# 06/21/16
# This program displays a recipe for baking two batches of
# cookies.

# Prints the instructions to make the batter
def makeBatter():
	print "Mix and dry ingredients."
	print "Cream the butter and sugar."
	print "Beat in the eggs."
	print "Stir in the dry ingredients."

# Prints the instructions to bake the cookies
def bake():
	print "Set the oven temperature."
	print "Set the timer."
	print "Place a batch of cookies to bake."
	print "Allow the cookies to bake."

# Prints the instructions to decorate the cookies
def decorate():
	print "Mix ingredients for frosting."
	print "Add frosting to cookie."

if __name__ == "__main__":
	makeBatter()
	bake()
	bake()
	decorate()