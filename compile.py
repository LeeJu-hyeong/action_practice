import sys
sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt','w')
try:
	n = int(sys.stdin.readline())

	

	ret = 0

	

	for i in range(n+1):

		ret += i

	

	print("Sum from 1 to n : {}".format(ret))

except Exception as e:
	print('Error Message: {}'.format(e))