fr = input('Digita uma frase:\n')
sp = fr.split()
print('')

for x in range(len(sp)):
    for y in range(len(sp) - x):
        print(sp[y+x], end = ' ')
    print('')

#for x in range(len(sp)):
    #print(*palavras)
    #palavras.remove(palavras[0])
#jeito do professor ^^^