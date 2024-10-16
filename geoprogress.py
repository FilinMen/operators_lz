input_data = open("input.txt","r")
data = input_data.read()
data = data.split()
b = int(data[0])
q = int(data[1])
n = int(data[2])

S = (b * (q ** n - 1))/(q - 1) # формула геометрической прогрессии 
S = int(S) # чтобы из 121.0 сделать 121
S = str(S) # чтобы закинуть в файл 

output_data = open("output.txt","w")
output_data.write(S)
output_data.close()
input_data.close()
