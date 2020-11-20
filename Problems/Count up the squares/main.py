# put your python code here
var = int(input())
sumvar = list()
sumvar.append(var)
loop_i = 0

while sum(sumvar) != 0:
    var = int(input())
    sumvar.append(var)
    loop_i += 1

for i in range(0, len(sumvar)):
    sumvar[i] = sumvar[i] * sumvar[i]

print(sum(sumvar))