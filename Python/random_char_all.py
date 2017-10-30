from random import randint
def randlist(r):
	alpha = ['!','"','#','$','%','&','\'','(',')','*',
	         '+',',','-','.','/','0','1','2','3','4',
	         '5','6','7','8','9',':',';','<','=','>',
	         '?','@','A','B','C','D','E','F','G','H',
	         'I','J','K','L','M','N','O','P','Q','R',
	         'S','T','U','V','W','X','Y','Z','[','\\',
	         ']','^','_','`','a','b','c','d','e','f',
	         'g','h','i','j','k','l','m','n','o','p',
	         'q','r','s','t','u','v','w','x','y','z',
	         '{','|','}','~']
	abcdefghijklmnopqrstuvwxyz = alpha[r]
	return alpha[r]
def main(randlist):
	done = False
	while done == False:
		r = randint(0,93)
		print(randlist(r),end=" ")
main(randlist)
randlist()
