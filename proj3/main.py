from pulp import *
import sys
# REPEAT
def is_winnable(team_id, n, matches, scores):

    filtered_matches = [m for m in matches if team_id in m]

    for min_matches in range(len(filtered_matches) + 1):
        prob = LpProblem("Minimize_score_to_win", LpMinimize)
        results = dict()

        # o meu jogo vai estar associado a este tuplo de variaveis em que consigo depois distunguir vitoria, perddido, ou empate

        for match in matches:
            win = LpVariable(f"win{match}",cat=LpBinary)
            tie = LpVariable(f"tie{match}",cat=LpBinary)
            loose = LpVariable(f"loose{match}",cat=LpBinary)

            results[match] = (win, tie, loose)
            
            # o jogo so pode ter um "estado" ou derrtoa ou empate ou vitoria
            prob += win + loose + tie == 1

        # isto é o objetivo do nosso problema
        # econtrar o numero minimo de jogos para ganhar
        team_wins = [] 

        for (i,j) in matches:
            # team é i logo usamos o indice 0 que indica a vitoria de i
            if i == team_id:
                team_wins.append(results[(i,j)][0])
            # team é j logo usamos o indice 2 que indica a derrota de i
            elif j == team_id:
                team_wins.append(results[(i,j)][2])
        

        # Objetivo basicamente
        prob += lpSum(team_wins) == min_matches

        # Calcular a soma de todos os jogos
        end_scores = {}
        for team in range(1, n + 1):
            points = []
            for (i, j) in matches:
                # mm cena de ha pouco
                # so um deles eq vai dar ent nem vale a pena manda if else
                if i == team:
                    points.append(3 * results[(i,j)][0] + results[(i,j)][1])
                elif j == team:
                    points.append(3 * results[(i,j)][2] + results[(i,j)][1])
            # usar os resultados anteriores para obter o reusltado final
            end_scores[team] = scores[team-1] + lpSum(points)
        
        for team in range(1, n + 1):
            if team != team_id:
                prob += end_scores[team_id] >= end_scores[team]

        prob.solve(PULP_CBC_CMD(msg=False))
        
        if LpStatus[prob.status] == "Optimal":
            return min_matches

    return -1

# função auxiliar para ter um dicionario com de jogos de cada equipa por fazer
def matches_left(n ,matches):
    new = []
    for i in range(1, n + 1):
        x = [k for [k, _] in matches.get(i)]
        for j in range(1, n + 1):
            if j not in x and i != j:
                new.append((i,j))
    return new

# N é o numero de equipas
# M é o numero de jogos ja realizados
def read_input():
    input_data = sys.stdin.read().strip().splitlines()
    n, m = map(int, input_data[0].split())
    
    matches = dict()

    scores = [0 for i in range(0, n)]

    for i in range(1, n + 1):
        matches[i] = []

    for i in range(1, m + 1):
        team1, team2, result = map(int, input_data[i].split()) 
        
        # por o jogo no dicionario
        matches[team1].append([team2, result])

        # por os resultados na lista (3 se ganhar, 1 se empatar, 0 se perder)
        if team1 == result:
            scores[team1 - 1] += 3
        elif team2 == result:
            scores[team2 - 1] += 3
        else:
            scores[team1 - 1] += 1
            scores[team2 - 1] += 1

    return n, m, matches, scores

n,m,matches,scores = read_input()
left = matches_left(n, matches)

for i in range(1, n + 1):
    val = is_winnable(i, n, left, scores)
    print(val)