import numpy as np
import numpy.ma as ma

visualizacao_stories = [
    [187, 120, 88, 70, 130, 168, 213],
    [0, 0, 42, 0, 0, 55, 77],
    [91, 0, 61, 0, 71, 121, 271],
    [0, 0, 0, 0, 187, 0, 0],
    [42, 23, 34, 0, 39, 29, 36]
]
pessoas = ['Raquel', 'Lucas', 'Daniel', 'Natalia', 'Anderson']
dias_semana = ['Domingo', 'Segunda', 'Terça',
               'Quarta', 'Quinta', 'Sexta', 'Sábado']

for x in range(len(pessoas)):
    print(pessoas[x] + "  -  Média de visualizações: " +
          str(np.mean(visualizacao_stories[x])))

somas_semana = []
for x in range(len(dias_semana)):
    soma = 0
    for y in range(5):
        soma = soma + visualizacao_stories[y][x]
    somas_semana.append(soma)

print("O Dia com maior visualização -> " + dias_semana[somas_semana.index(max(somas_semana))] +
      " com " + str(somas_semana[somas_semana.index(max(somas_semana))])+" Visualizações")
# Indice do dia com maior soma de visualizações

print("---------------------------------------------")

visualizacao_stories_invalidos = np.array([
    [52, 68, 97, 55, -1, 98, -1],
    [53, -1, 38, -1, -1, 72, 49],
    [88, -1, 64, -1, 77, 130, 43],
    [-1, 30, -1, -1, -1, 182, -1],
    [41, 20, 33, -1, 37, 23, 7]
])

array_mascarado = np.ma.masked_where(
    visualizacao_stories_invalidos < 0, visualizacao_stories_invalidos)


for x in range(len(pessoas)):
    print(pessoas[x] + "  -  Média de visualizações: " +
          str(np.mean(array_mascarado[x])))

somas_semana2 = []
for x in range(len(dias_semana)):
    soma = 0
    for y in range(5):
        if(visualizacao_stories_invalidos[y][x] > -1):
            soma = soma + visualizacao_stories_invalidos[y][x]
    somas_semana2.append(soma)

print("O Dia com maior visualização -> " + dias_semana[somas_semana2.index(max(somas_semana2))] +
      " com " + str(somas_semana2[somas_semana2.index(max(somas_semana2))])+" Visualizações")
