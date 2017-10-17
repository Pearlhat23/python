from random import randint
def randlist(r,usedlist,done):
	sum = 0
	alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
	usedlist[r] = 1
	c = alpha[r]
	
	for i in range (len(usedlist)):
		sum = sum + usedlist[i]
	print (c,usedlist," sum ", sum)
	if sum == 6:
		done = True
	return c,usedlist,done

def main():
	used = [0,0,0,0,0,0]
	done = False
	##########################
	while done == False:
		r = randint(0,5)
		c,used,done = randlist(r,used,done)
		#print (used)
		print(c,end=" ")
main()
