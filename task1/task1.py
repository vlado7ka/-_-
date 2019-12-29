import numpy as np
from statistics import median
import sys

if __name__ == "__main__":
    for param in sys.argv:
        args = param

s = []
k = []
with open(args, "r") as file:
    for line in file:
        s.append(line)
for i in s:
	if i != '\n':
		k.append(int(i))
a = np.array(k) 
p = np.percentile(a, 90) 
print(f'{p:.{2}f}')
print(f'{median(k):.{2}f}')
print(f'{max(k):.{2}f}')
print(f'{min(k):.{2}f}')
print(f'{np.mean(k):.{2}f}')
