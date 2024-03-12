n = []
n.append(int(input()))
n.append(int(input()))
n.append(int(input()))
n.append(int(input()))
p = []

for x in range(0, len(n)):
    if (n[x])%2 == 0:
        p.append(n[x])

if p == []:
    print('Nenhum valor par encontrado.')
else:  
    z = p[0]
    for y in range(0, (len(p) - 1)):
        if p[y+1] > p[y]:
            z = p[y+1]
    
    print(f'Maior número par = {z}')