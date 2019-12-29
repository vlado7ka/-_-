import sys

args=[]
if __name__ == "__main__":
    for param in sys.argv:
        args = param 

s = []
k = []
for i in range(1,6):
	with open(args + 'Cash' + str(i) + '.txt', "r") as file:
	    for line in file:
	    	if line[-1] == '\n':
	    		s.append(float(line[:-1]))
	    	else:
	    		s.append(float(line))
	k.append(s)
	s = []

n=0
for x in zip(*k):
	s.append(sum(x))
	if n < sum(x):
		n = sum(x)

print(s.index(n)+1)
