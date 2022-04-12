notas_rock = [5, 1, 4, 0, 2, 5, 2, 1, 0, 5, 5, 3, 5, 2, 5, 5, 3, 5, 4, 4]
notas_pop = [3, 2, 5, 1, 2, 1, 4, 1, 5, 0, 4, 2, 1, 2, 5, 2, 4, 4, 0, 1]

ruins_rock = list(map(lambda x: x < 2, notas_rock))
medianas_rock = list(map(lambda x: (x > 1 and x < 4), notas_rock))
boas_rock = list(map(lambda x: x > 3, notas_rock))

ruins_pop = list(map(lambda x: x < 2, notas_pop))
medianas_pop = list(map(lambda x: (x > 1 and x < 4), notas_pop))
boas_pop = list(map(lambda x: x > 3, notas_pop))


def qtdBoas(r, p):  # Funcao para a ultima pergunta
    if r > p:
        return "Rock"
    else:
        return "POP"


print("Musicas Ruins Rock: " +
      str(len(list(filter(lambda x: x == True, ruins_rock)))))

print("Musicas Medianas Rock: " +
      str(len(list(filter(lambda x: x == True, medianas_rock)))))

print("Musicas Boas Rock: " +
      str(len(list(filter(lambda x: x == True, boas_rock)))))

print("------")

print("Musicas Ruins POP: " +
      str(len(list(filter(lambda x: x == True, ruins_pop)))))

print("Musicas Medianas POP: " +
      str(len(list(filter(lambda x: x == True, medianas_pop)))))

print("Musicas Boas POP: " +
      str(len(list(filter(lambda x: x == True, boas_pop)))))

print("------")

print("Existe alguma musica mediana de Rock ? " + str(any(medianas_rock)))
print("Todas as musicas de POP são boas ? " + str(all(boas_pop)))

MaisBoas = qtdBoas(len(list(filter(lambda x: x == True, boas_rock))),
                   len(list(filter(lambda x: x == True, boas_pop))))
print("Qual genero de musica teve uma maior quantidade de músicas boas ? " + MaisBoas)
