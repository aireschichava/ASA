from pulp import *
import sys

def max_toys_satisfied(factories, countries, requests):
    # Filtrar fábricas com estoque > 0
    factories = [factory for factory in factories if factory[2] > 0]
    valid_factory_ids = {factory[0] for factory in factories}

    # Atualizar pedidos para considerar apenas fábricas válidas
    filtered_requests = [
        (k[0], k[1], *[i for i in k[2:] if i in valid_factory_ids])
        for k in requests
    ]

    # Remover pedidos que ficaram sem fábricas válidas
    filtered_requests = [k for k in filtered_requests if len(k) > 2]

    prob = LpProblem("Maximize_Satisfied_Children", LpMaximize)

    # Variáveis de decisão
    x = LpVariable.dicts("x", ((k[0], i) for k in filtered_requests for i in k[2:]),
                         0, 1, cat="Continuous")

    # Objetivo: Maximizar o número de crianças satisfeitas
    prob += lpSum(x[k[0], i] for k in filtered_requests for i in k[2:])

    # Restrições:
    # Cada criança pode receber no máximo um presente
    for k in filtered_requests:
        prob += lpSum(x[k[0], i] for i in k[2:]) <= 1

    # Estoque máximo de cada fábrica
    for factory in factories:
        i, j, max_stock = factory
        prob += lpSum(x[k[0], i] for k in filtered_requests if i in k[2:]) <= max_stock

    # Restrições de exportação e entrega mínima por país
    for country in countries:
        j, max_export, min_toys = country

        # Exportação máxima de fábricas no país `j`
        prob += lpSum(
            x[k[0], i] for k in filtered_requests for i in k[2:]
            if factories[i - 1][1] == j and k[1] != j
        ) <= max_export

        # Mínimo de brinquedos entregues no país `j`
        prob += lpSum(
            x[k[0], i] for k in filtered_requests for i in k[2:] if k[1] == j
        ) >= min_toys

    # Resolver o problema
    prob.solve(PULP_CBC_CMD(msg=False))

    # Verificar viabilidade e retornar resultado
    if LpStatus[prob.status] == "Optimal":
        return int(sum(x[k[0], i].varValue for k in filtered_requests for i in k[2:]))
    else:
        return -1

# Leitura da entrada
def read_input():
    input_data = sys.stdin.read().strip().splitlines()
    n, m, t = map(int, input_data[0].split())

    factories = []
    for i in range(1, n + 1):
        factories.append(tuple(map(int, input_data[i].split())))

    countries = []
    for i in range(n + 1, n + m + 1):
        countries.append(tuple(map(int, input_data[i].split())))

    requests = []
    # Registrar o número de crianças por país
    kid_per_country = {}
    for i in range(n + m + 1, n + m + t + 1):
        request = list(map(int, input_data[i].split()))
        if kid_per_country.get(request[1]) == None:
            kid_per_country[request[1]] = 1
        else:
            kid_per_country[request[1]] += 1
        requests.append(request)

    # Verificar se o número de crianças em um país é menor que o número mínimo de brinquedos
    for country in countries:
        if kid_per_country.get(country[0]) == None:
            country[2] = 0
        elif country[2] > kid_per_country[country[0]]:
            country[2] = kid_per_country[country[0]]

    for request in requests:
        for factory_index in range(0, len(request[2:])):
            if factories[request[factory_index + 2] - 1][2] == 0:
                factories.pop(request[factory_index + 2] - 1)
                requests.pop(factory_index + 2)

    return factories, countries, requests

# Executar o programa
try:
    factories, countries, requests = read_input()
    output = max_toys_satisfied(factories, countries, requests)
    print(output)
except:
    print(-1)