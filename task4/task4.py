import numpy as np
import sys

if __name__ == "__main__":
    for param in sys.argv:
        args = param
s = []
with open(args, 'r') as file:
    for line in file:
        s.append(line.split('\n')[0])

k = []
start = tuple()
for i in s:
	k.append(((int(i.split()[0].split(':')[0])*60 + int(i.split()[0].split(':')[1])), (int(i.split()[1].split(':')[0])*60 + int(i.split()[1].split(':')[1]))))
k = tuple(k)

p = {}
for i in k:
	for j in range(2):
		p[i[j]] = 0
for i in k:
	for j in p:
		if i[0] <= j < i[1]:
			p[j] += 1

nmax = 0
for i in p.values():
	if nmax <= i:
		nmax = i

dictans = {}
for i in sorted(p.keys()):
	dictans[i] = p[i]
listans = []
for i, j in dictans.items():
	if j == nmax:
		listans.append(i)

l = [i for i in dictans]

s = [[listans[0], listans[1]]]
for i in listans:
	if i in l:
		if i == s[-1][1]:
			s[-1][1] = l[l.index(i)+1]
		elif s[-1][0] == i and s[-1][1] <= l[l.index(i)+1]:
			s[-1][1] = l[l.index(i)+1]
		elif s[-1][0] == i and s[-1][1] > l[l.index(i)+1]:
			continue
		else:
			s.append([i, l[l.index(i)+1]])

k = []
for i in s:
	for j in i:
		s[s.index(i)][i.index(j)] = str(j//60) +':'+str(j%60)

for i in s:
	for j in i:
		if len(j[j.index(':')+1:]) < 2:
			s[s.index(i)][i.index(j)] += '0'

for i in s:
	print(*i)


