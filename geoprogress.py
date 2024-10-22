ingeoprogress_data = open("ingeoprogress.txt","r")
data = ingeoprogress_data.read()
data = data.split()
b = int(data[0])
q = int(data[1])
n = int(data[2])

S = (b * (q ** n - 1))/(q - 1) # формула геометрической прогрессии 
S = int(S) # чтобы из 121.0 сделать 121
S = str(S) # чтобы закинуть в файл 

outgeoprogress_data = open("outgeoprogress.txt","w")
outgeoprogress_data.write(S)
outgeoprogress_data.close()
ingeoprogress_data.close()
