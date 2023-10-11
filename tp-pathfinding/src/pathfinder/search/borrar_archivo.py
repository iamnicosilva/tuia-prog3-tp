diccionario = {}
diccionario[(7,6)]=7
diccionario[(6,6)]=99
diccionario[(3,6)]=1
diccionario[(8,6)]=68
print(max(diccionario,key=diccionario.get))