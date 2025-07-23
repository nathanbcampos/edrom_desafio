# NOME DO CANDIDATO: Nathan Bernardes Campos
# CURSO DO CANDIDATO: Engenharia Mecatrônica
# AREAS DE INTERESSE: Behavior e elétrica

# Você pode importar as bibliotecas que julgar necessárias.
import math

def encontrar_caminho(pos_inicial, pos_objetivo, obstaculos, largura_grid, altura_grid, tem_bola=False):
    """
    Esta é a função principal que você deve implementar para o desafio EDROM.
    Seu objetivo é criar um algoritmo de pathfinding (como o A*) que encontre o
    caminho ótimo para o robô, considerando os diferentes níveis de complexidade.

    Args:
        pos_inicial (tuple): A posição (x, y) inicial do robô.
        pos_objetivo (tuple): A posição (x, y) do objetivo (bola ou gol).
        obstaculos (list): Uma lista de tuplas (x, y) com as posições dos obstáculos.
        largura_grid (int): A largura do campo em células.
        altura_grid (int): A altura do campo em células.
        tem_bola (bool): Um booleano que indica o estado do robô.
                         True se o robô está com a bola, False caso contrário.
                         Este parâmetro é essencial para o Nível 2 do desafio.

    Returns:
        list: Uma lista de tuplas (x, y) representando o caminho do início ao fim.
              A lista deve começar com o próximo passo após a pos_inicial e terminar
              na pos_objetivo. Se nenhum caminho for encontrado, retorna uma lista vazia.
              Exemplo de retorno: [(1, 2), (1, 3), (2, 3)]

    ---------------------------------------------------------------------------------
    REQUISITOS DO DESAFIO (AVALIADOS EM NÍVEIS):
    ---------------------------------------------------------------------------------
    [NÍVEL BÁSICO: A* Comum com Diagonal]
    O Algoritmo deve chegar até a bola e depois ir até o gol (desviando dos adversários) 
    considerando custos diferentes pdra andar reto (vertical e horizontal) e para andar em diagonal

    [NÍVEL 1: Custo de Rotação]
    O custo de um passo não é apenas a distância. Movimentos que exigem que o robô
    mude de direção devem ser penalizados. Considere diferentes penalidades para:
    - Curvas suaves (ex: reto -> diagonal).
    - Curvas fechadas (ex: horizontal -> vertical).
    - Inversões de marcha (180 graus).

    [NÍVEL 2: Custo por Estado]
    O comportamento do robô deve mudar se ele estiver com a bola. Quando `tem_bola`
    for `True`, as penalidades (especialmente as de rotação do Nível 1) devem ser
    AINDA MAIORES. O robô precisa ser mais "cuidadoso" ao se mover com a bola.

    [NÍVEL 3: Zonas de Perigo]
    As células próximas aos `obstaculos` são consideradas perigosas. Elas não são
    proibidas, mas devem ter um custo adicional para desencorajar o robô de passar
    por elas, a menos que seja estritamente necessário ou muito vantajoso.

    DICA: Um bom algoritmo A* é flexível o suficiente para que os custos de movimento
    (g(n)) possam ser calculados dinamicamente, incorporando todas essas regras.
    """

    # -------------------------------------------------------- #
    #                                                          #
    #             >>>  IMPLEMENTAÇÃO DO CANDIDATO   <<<        #
    #                                                          #
    # -------------------------------------------------------- #
    x_atual, y_atual = pos_inicial
    x_objetivo, y_objetivo = pos_objetivo
    direcao_anterior  = (0,0)   #Inicializa direcao (x = 0, y = 0)
    

    caminho = []

    #Enquanto as posições forem diferentes calcula melhor passo
    while (x_atual, y_atual) != (x_objetivo, y_objetivo):
        mov_posiveis = [
            (1, 0), (-1, 0), #Direção Horizontal
            (0, 1), (0, -1), #Direção Vertical
            (1, 1), (-1, -1), #Diagonal
            (1, -1), (-1, 1)  #Diagonal
        ]

        melhor_f = float('inf') #Garante que o primeiro movimento sempre seja o melhor
        melhor_passo = None

        for dx, dy in mov_posiveis:
            nx, ny = x_atual + dx, y_atual + dy 

            if not (0 <= nx < largura_grid and 0 <= ny < altura_grid):
                continue

            if (nx, ny) in obstaculos: # Evita os obstaculos
                continue

            g = math.hypot(dx, dy) #Custo do movimento
            penalidade = 0

            if direcao_anterior != (0,0):
                if  (dx, dy) == (-direcao_anterior[0], -direcao_anterior[1]): #Inversao completa de direcao 180 graus
                    penalidade = penalidade + 2

                #Se dx + dy == 2 movimento diagonal se a soma de dx + dy = 1 movimento é reto
                elif (abs(dx) + abs(dy) == 2) and (abs(direcao_anterior[0]) + abs(direcao_anterior[1] == 1)): # Mudança de direção de movimento reto para diagonal
                    penalidade = penalidade + 1
                # movimento reto                      e movimento anterior era também reto o                novo movimento tem que ser diferente do anterior
                elif (abs(dx) + abs(dy) == 1) and (abs(direcao_anterior[0]) + abs(direcao_anterior[1] == 1)) and (dx != direcao_anterior[0] or dy != direcao_anterior[1]) :
                    penalidade = penalidade + 3

                if tem_bola == True:
                    penalidade = penalidade*2

             #Pegar posição x e y de todos os obstáculos
            #for x_obstaculos, y_obstaculos in obstaculos:
                #dif_x = nx - x_obstaculos
                #dif_y = ny - y_obstaculos 
                #se a distancia entre o robô e o obstáculo for menor ou igual à raiz de 2 (menor distancia possível entre o robo e o obstaculo) entao sera aplicado outra penalidade
                #if math.hypot(dif_x, dif_y) <= math.sqrt(2):
                    #penalidade = penalidade + 3

            g = g + penalidade # Soma a penalidade
            h = math.hypot(x_objetivo - nx, y_objetivo - ny) #Distancia até o objetivo
            f = g + h #Algoritmo A*

            #Substitui o melhor o novo melhor caminho
            if f < melhor_f:
                melhor_f = f
                melhor_passo = (nx, ny)
                nova_direcao = (dx, dy)

        direcao_anterior = nova_direcao
        if melhor_passo is None:
            return []

        x_atual, y_atual = melhor_passo
        caminho.append(melhor_passo)

    return caminho

    # O código abaixo é um EXEMPLO SIMPLES de um robô que apenas anda para frente.
    # Ele NÃO desvia de obstáculos e NÃO busca o objetivo.
    # Sua tarefa é substituir esta lógica simples pelo seu algoritmo A* completo.

    # print("Usando a função de exemplo: robô andando para frente.")
    
    # caminho_exemplo = []
    # x_atual, y_atual = pos_inicial

    # # Gera um caminho de até 10 passos para a direita (considerado "frente" no campo)
    # for i in range(1, 11):
    #     proximo_x = x_atual + i
        
    #     # Garante que o robô não tente andar para fora dos limites do campo
    #     if proximo_x < largura_grid:
    #         caminho_exemplo.append((proximo_x, y_atual))
    #     else:
    #         # Para o loop se o robô chegar na borda do campo
    #         break

    # # Retorna o caminho
    # return caminho_exemplo
