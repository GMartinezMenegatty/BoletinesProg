abecedario = [chr(i)for i in range(97, 123)]
abc = []
t = 1

for letras in abecedario:
    if t % 3 != 0:
        abc.append(letras)
    t += 1


print(abc)
