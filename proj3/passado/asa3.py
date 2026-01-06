from pulp import *
import sys

def max_toys_satisfied(factories,countries,requests):
    adjusted_requests = []
    for request in requests:
        # Manter apenas fábricas válidas no pedido da criança
        valid_factories_for_request = [i for i in request[2:] if factories[i-1][2] > 0]
        if len(valid_factories_for_request) > 0:
            # Adicionar pedido ajustado (se ainda houver fábricas válidas)
            adjusted = [request[0], request[1]] + valid_factories_for_request
            adjusted_requests.append(adjusted)

    adjusted_factories = [factory for factory in factories if factory[2] > 0]
    prob = LpProblem("Maximize_Satisfied_Children", LpMaximize)

    # A variavel "x" é um dicionario que guarda o numero de presentes que cada criança recebeu
    # a criança pode ou receber nada ou so um no maximo então so pode variar enre 0 e 1 o valor no dicionario
    
    # k[0] ==> id da criança
    # i ==> id da fabrica do brinquedo que a criança pediu
    
    #time limit exceeded ent lave usar outra cena
    x = LpVariable.dicts("x", ((k[0], i) for k in adjusted_requests for i in k[2:]), 0, 1, cat="Continuous")
    # Objetivo:
    # maximizar o numero de crinças que recebem presente
    # logo vai ser a soma de todas as entradas na nossa variavel "x"
    prob += lpSum(x[k[0], i] for k in adjusted_requests for i in k[2:])

    # Restrições:
    # Cada criança so pode ter no maximo um presente
    for k in adjusted_requests:
        prob += lpSum(x[k[0], i] for i in k[2:]) <= 1

    # Cada fabrica pode so produzir no maximo "max_stock" elementos
    for factory in adjusted_factories:
        # i ==> identificador da fabrica
        # j ==> identificador do pais em que a fabrica esta
        # max_stock ==> limite de produção maximo da fabrica 
        i, j, max_stock = factory
        # a soma de todos os brinquedos produzidos da fabrica "i" não pode exceder o "max_stock"
        prob += lpSum(x[k[0], i] for k in adjusted_requests if i in k[2:]) <= max_stock

    # Cada pais tem de ter no minimo "min_toys" brinquedos distribuidos
    # Cada pais so pode no maximo exportar "max_export" brinquedos exportados
    for country in countries:
        # j ==> identificador do pais
        # max_export ==> limite de exportação maximo do pais
        # min_toys ==> limite de distribuição minimo do fabrica
        j, max_export, min_toys = country
        
        prob += lpSum(x[k[0], i] for k in adjusted_requests for i in k[2:] if k[1] == j) >= min_toys
        
        prob += lpSum(x[k[0], i] for k in adjusted_requests for i in k[2:] if (k[1]!= j and adjusted_factories[i - 1][1] == j)) <= max_export
        # a soma de todos os briquedos distribuidos para as crianças do pais "j" tem de ser maior que "min_toys"
        

    # Solve the problem
    prob.solve(PULP_CBC_CMD(msg=False))
    # Check feasibility and return result
    if LpStatus[prob.status] == "Optimal":
        return int(sum(x[k[0], i].varValue for k in adjusted_requests for i in k[2:]))
    else:
        return -1

#  python3 projeto_asa.py < input.txt
def read_input():
    input_data = sys.stdin.read().strip().splitlines()
    n, m, t = map(int, input_data[0].split())
    
    factories = []
    for i in range(1, n + 1):
        factories.append(list(map(int, input_data[i].split())))
    
    countries = []
    for i in range(n + 1, n + m + 1):
        countries.append(list(map(int, input_data[i].split())))
    
    requests = []
    # regista o numero de crianlaças por cada pais
    for i in range(n + m + 1, n + m + t + 1):
        requests.append(list(map(int, input_data[i].split())))
    
    return factories, countries, requests

try:
    factories, countries, requests = read_input()
    output1 = max_toys_satisfied(factories, countries, requests)
    print(output1) 
except:
    print(-100)