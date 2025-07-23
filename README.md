# Desafio Individual EDROM - Robô A*



# 1.Introdução do Problema

Este projeto apresenta uma solução para o desafio de pathfinding (busca de caminho) proposto pela Edrom. O objetivo é desenvolver uma função encontrar_caminho em Python que guie um robô de forma autônoma em um campo 2D representado por um grid.

Levando em conta os seguintes pontos:

* Encontrar o melhor caminho até o objetivo.
* Utilizar diferentes comportamentos levando em conta o custo da movimentação, posse de bola e proximidade dos adversários.

# 2.Abordagem da solução

Foi utilizado o algoritmo basedo no algoritmo A* para a resolução do desafio:

    f = g + h

onde:
* `g` representa o custo real desde o início até o nó atual.
* `h` representa o custo estimado do nó atual até a meta.

De início é necessário estabelecer o loop principal e os possíveis movimentos do robô:

```python
while (x_atual, y_atual) != (x_objetivo, y_objetivo):
    mov_posiveis = [
            (1, 0), (-1, 0), #Direção Horizontal
            (0, 1), (0, -1), #Direção Vertical
            (1, 1), (-1, -1), #Diagonal
            (1, -1), (-1, 1)  #Diagonal
        ]
```

Inicialização de varíaveis auxiliares:
```python
melhor_f = float('inf') #Garante que o primeiro movimento sempre seja o melhor
melhor_passo = None
```
E para cada possível movimento será estabelecido o novo movimento, suas limitações e o custo do movimento:

```python
for dx, dy in mov_posiveis:
    nx, ny = x_atual + dx, y_atual + dy 

    if not (0 <= nx < largura_grid and 0 <= ny < altura_grid):
        continue

    if (nx, ny) in obstaculos: # Evita os obstaculos
        continue

    g = math.hypot(dx, dy)
    penalidade = 0
```
e para a implementação das penalidades:

```python
if direcao_anterior != (0,0):
    if  (dx, dy) == (-direcao_anterior[0], -direcao_anterior[1]): #Inversao completa de direcao 180 graus
        penalidade = penalidade + 2


    elif (abs(dx) + abs(dy) == 2) and (abs(direcao_anterior[0]) + abs(direcao_anterior[1] == 1)): # Mudança de direção de movimento reto para diagonal
        penalidade = penalidade + 1
    
    elif (abs(dx) + abs(dy) == 1) and (abs(direcao_anterior[0]) + abs(direcao_anterior[1] == 1)) and (dx != direcao_anterior[0] or dy != direcao_anterior[1]) :
        penalidade = penalidade + 3

    if tem_bola == True:
        penalidade = penalidade*2
```

Calculo final do custo:

```python
g = g + penalidade # Soma a penalidade
h = math.hypot(x_objetivo - nx, y_objetivo - ny) #Distancia até o objetivo
f = g + h #Algoritmo A*
```

Para a atualização do melhor passo:

```python
 if f < melhor_f:
    melhor_f = f
    melhor_passo = (nx, ny)
    nova_direcao = (dx, dy)
```

Assim para finalizar a implementação o seguinte trecho para atualizar a posição:

```python
direcao_anterior = nova_direcao
if melhor_passo is None:
    return []

x_atual, y_atual = melhor_passo
caminho.append(melhor_passo)
```

# 3.Conclusão

Respeitando a proposta do desafio, este foi a forma mais eficiente que encontrei para a resolução do problema. Assim , tendo como características a modularidade e a simplicidade, considerando a possibilidade de novas abordagens e outras estratégias com aplicações reais em simulação.

Desenvolvido por Nathan Bernardes Campos
