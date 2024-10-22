inoperations_data = open("inoperations.txt","r")
data = inoperations_data.read()
n = int(data)
t = 0 # вводим для подсчета циклов с 0
while n != 0: # пока n небудет равно нулю циклы будут продолжаться 
    if n % 3 == 0: # первое условие
        n -= 3
    elif n % 3 == 1: # второе условие 
        n -=1
    else:
        n -= 2 
    t += 1
t = str(t)
outoperations_data = open("outoperations.txt","w")
outoperations_data.write(t)
inoperations_data.close()
outoperations_data.close()