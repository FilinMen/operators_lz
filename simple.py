insimple_data = open("insimple.txt","r")
data = insimple_data.read()
a = int(data)
if a == 1 or a == 3 or a == 5 or a == 7 or a == 11 or a == 13 or a == 17 or a == 19 or a == 23: # проверяем на совпадение числа (a) с простыми числами
 x = "Y" # число а простое 
else:
 x = "N" # число а непростое 
outsimple_data = open("outsimple.txt","w")
outsimple_data.write(x)
outsimple_data.close()
insimple_data.close()