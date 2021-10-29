import nashpy as nash
import numpy as np

def weight(task):
	return task[1]

def value(task):
	return task[2]

def cost_per_weight_unit(task_weight, resources_available):
    if (resources_available/task_weight >= 10):
        return 0.2
    elif (resources_available/task_weight >= 5):
        return 0.4
    elif (resources_available/task_weight >= 2.5):
        return 0.6
    elif (resources_available/task_weight >= 1):
        return 0.8
    else: 
        return 1

def gta(W, T):

    VCC=[]
    for i,j in W.items():
        VCC.append(j)

    Tarefas_alocadas = []
    peso_acumulado = 0
    valor_acumulado = 0
    Tarefas = sorted(T, key=weight, reverse=True)

    while len(Tarefas) > 0:
        tarefa = Tarefas.pop(0)
        index_max = VCC.index(max(VCC))
        max_resource = max(VCC)
        if (max_resource >= weight(tarefa)):

            p1_11 = value(tarefa) - (weight(tarefa) * cost_per_weight_unit(weight(tarefa), max_resource))
            p1_12 = -value(tarefa)
            p1_21 = -2*value(tarefa)
            p1_22 = 0
            player1 = np.array([[p1_11, p1_12], [p1_21, p1_22]])

            p2_11 = weight(tarefa) * cost_per_weight_unit(weight(tarefa), max_resource)
            p2_12 = -2 * weight(tarefa) * cost_per_weight_unit(weight(tarefa), max_resource)
            p2_21 = -weight(tarefa) * cost_per_weight_unit(weight(tarefa), max_resource)
            p2_22 = 0
            player2 = np.array([[p2_11, p2_12], [p2_21, p2_22]])

            Matriz_de_Recompensa = nash.Game(player1, player2)
        
            eqs = Matriz_de_Recompensa.support_enumeration()
            nash_equilibrium = list(eqs)

            if ((nash_equilibrium[0][0] == [1., 0.]).all() and (nash_equilibrium[0][1] == [1., 0.]).all()):
                Tarefas_alocadas.append(tarefa)
                VCC[index_max] -= weight(tarefa)
                peso_acumulado += weight(tarefa)
                valor_acumulado += value(tarefa)
                
        else: continue

    return valor_acumulado, len(Tarefas_alocadas), peso_acumulado
