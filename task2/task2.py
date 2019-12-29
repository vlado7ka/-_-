import sys

args=[]
if __name__ == "__main__":
    for param in sys.argv:
        args.append(param)     

file1, file2 = [], []
with open(args[1], 'r') as file:
    for line in file:
        if line[-1] == '\n':
            file1.append(line[:line.index('\n')].split())
        else:
            file1.append(line.split())
            
with open(args[2], 'r') as file:
    for line in file:
        if line[-1] == '\n':
            file2.append(line[:line.index('\n')+1].split())
        else:
            file2.append(line.split())

#Функция "inPolygon" заимствована с Википедии
def inPolygon(x, y, xp, yp):
    c=0
    for i in range(len(xp)):
        if (((yp[i]<=y and y<yp[i-1]) or (yp[i-1]<=y and y<yp[i])) and \
            (x > (xp[i-1] - xp[i]) * (y - yp[i]) / (yp[i-1] - yp[i]) + xp[i])): c = 1 - c    
    return c            
            
for i in file2:
    if i in file1: 
        print(0) # точка на одной из вершин
    elif float(file1[0][0]) <= float(i[0]) <= float(file1[1][0]) and float(file1[0][1]) <= float(i[1]) <= float(file1[1][1]) or float(file1[1][0]) <= float(i[0]) <= float(file1[2][0]) and float(file1[1][1]) <= float(i[1]) <= float(file1[2][1]) or float(file1[2][0]) <= float(i[0]) <= float(file1[3][0]) and float(file1[2][1]) <= float(i[1]) <= float(file1[3][1]) or float(file1[0][0]) <= float(i[0]) <= float(file1[3][0]) and float(file1[0][1]) <= float(i[1]) <= float(file1[3][1]): 
        print(1) # точка на одной из сторон
    elif inPolygon(float(i[0]), float(i[1]), (float(file1[0][0]), float(file1[1][0]), float(file1[2][0]), float(file1[3][0])), (float(file1[0][1]), float(file1[1][1]), float(file1[2][1]), float(file1[3][1]))):
        print(2) # точка внутри
    else: 
        print(3) #точка снаружи
        
