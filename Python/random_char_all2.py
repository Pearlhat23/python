from random import randint
def randlist(r, done, used):
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
	
	used[r] = 1
	#print(alpha, used)
	return alpha[r], done
	
def main():
	used = [0] * 94
	done = False
	while done == False:	
		for i in range(len(used)):
			sum = 0
			r = randint(0,93)
			c, done = randlist(r, done, used)
			#print(len(used))
			sum = sum + used[i]
			if sum == 94:
				done = True
		print(c, end=" ")
main()
