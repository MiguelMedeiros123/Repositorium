f = input('Digita uma frase\n')
s = 0
for x in f:
    if '0' <= x <= '9': s += int(x)
print(s)

#['0', '1', ..., '8', '9'] e 'and' também funcionam