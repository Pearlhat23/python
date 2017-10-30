from random import randint
def randlist(r):
	alpha = ["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "01234567890",]
	abcdefghijklmnopqrstuvwxyz = alpha[r]
	return alpha[r]
def main(randlist):
	done = False
	while done == False:
		r = randint(0,2)
		print(randlist(r),end=" ")
main(randlist)
randlist()
