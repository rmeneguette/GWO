#!/usr/bin/env python
# Joahannes B. D. da Costa <joahannes@lrc.ic.unicamp.br>

import log_manager
import random
import copy

import time

import gwo_modelo
import BAT
import gta_modelo
# Estrutura das tarefas e como serao alocadas

# W   = capacidade da mochila
# wt  = peso da tarefa
# val = valor da tarefa (ganho)
# n   = numero de tarefas

def task_allocation(step, W, T):
	# W = vccs set
	# T = tasks set

	T1 = copy.copy(T) #dp
	T2 = copy.copy(T) #greedy-weight
	T3 = copy.copy(T) #greedy-value
	T4 = copy.copy(T) #greedy-n
	T5 = copy.copy(T) #mors
	T6 = copy.copy(T) #gwo
	T7 = copy.copy(T) #bat
	T8 = copy.copy(T) #gta


	dp = True
	greedy = True
	mors_s = False
	dp_random = False
	greedy_value = False
	greedy_new = True
	gwo = False
	bat = False
	gta = True

	soma = 0
	maior = 0
	for i,j in W.items():
		soma += j
		if j > maior:
			maior = j

	tamanho_t_mors = len(T)
	n_vccs = len(W)

	# print "MAIOR VCC:",maior

	if greedy == True:
		# print "GREEDY-WEIGHT:",greedy_solution(maior, T)
		inicio_g1 = time.time()
		ganho_greedy, n_greedy, peso_greedy = greedy_solution(maior, T)
		final_g1 = time.time()
		total_g1 = final_g1 - inicio_g1
		log_manager.log_allocation(step, soma, len(T), 0, ganho_greedy, n_greedy, n_vccs, peso_greedy, total_g1)

	if dp == True:
		# for DP solution
		wt = []
		T1 = []
		for i in T:
			wt.append(i[1])
			T1.append(i[2])

		# print "DP:",dp_solution(maior, wt, T1)
		inicio_dp = time.time()
		ganho_dp, n_dp, peso_dp = dp_solution(maior, wt, T1)
		final_dp = time.time()
		total_dp = final_dp - inicio_dp
		log_manager.log_allocation(step, soma, len(T), 1, ganho_dp, n_dp, n_vccs, peso_dp, total_dp)

	if greedy_value == True:
		# print "GREEDY-VALUE:",greedy_solution_value(maior, T)
		ganho_greedy_value, n_greedy_value, peso_greedy_value = greedy_solution_value(maior, T3)
		log_manager.log_allocation(step, soma, tamanho_t_mors, 3, ganho_greedy_value, n_greedy_value, n_vccs, peso_greedy_value)

	if mors_s == True:
		# print "MORS:",mors(W, T, True)
		inicio_mors = time.time()
		ganho_mors, n_mors, peso_mors = mors(W, T5, True)
		final_mors = time.time()
		total_mors = final_mors - inicio_mors
		log_manager.log_allocation(step, soma, tamanho_t_mors, 2, ganho_mors, n_mors, n_vccs, peso_mors, total_mors)

	if gwo == True:
		inicio_mors = time.time()
		ganho_mors, n_mors, peso_mors = gwo_modelo.gwo(W, T6)
		final_mors = time.time()
		total_mors = final_mors - inicio_mors
		log_manager.log_allocation(step, soma, tamanho_t_mors, 5, ganho_mors, n_mors, n_vccs, peso_mors, total_mors)

	if bat == True:
		inicio_bat = time.time()
		ganho_bat, n_bat, peso_bat = BAT.bat(W, T7)
		final_bat = time.time()
		total_bat = final_bat - inicio_bat
		log_manager.log_allocation(step, soma, tamanho_t_mors, 10, ganho_bat, n_bat, n_vccs, peso_bat, total_bat)

	if greedy_new == True:
		#("MORS:",mors(W, T, True)
		ganho_mors = 0
		n_mors = 0
		peso_mors = 0

		inicio_greedy = time.time()
		ganho_mors, n_mors, peso_mors = greedy_mors(W, T4, True)
		final_greedy = time.time()
		total_greedy = final_greedy - inicio_greedy
		log_manager.log_allocation(step, soma, tamanho_t_mors, 4, ganho_mors, n_mors, n_vccs, peso_mors, total_greedy)

	if gta == True:
		inicio_gta = time.time()
		ganho_gta, n_gta, peso_gta = gta_modelo.gta(W, T8)
		final_gta = time.time()
		total_gta = final_gta - inicio_gta
		log_manager.log_allocation(step, soma, tamanho_t_mors, 6, ganho_gta, n_gta, n_vccs, peso_gta, total_gta)

# ============================================================
# 						BRUTE FORCE
# ============================================================

# for brute force solution (tasks combinations)
def powerset(items):
	res = [[]]
	for item in items:
		newset = [r+[item] for r in res]
		res.extend(newset)
	return res

def brute_force_solution(W, T):

	knapsack = []
	best_weight = 0
	best_value = 0

	for item_set in powerset(T):

		set_value = sum([e[2] for e in item_set])
		set_weight = sum([e[1] for e in item_set])

		if set_value > best_value and set_weight <= W:
			best_value = set_value
			best_weight = set_weight
			knapsack = item_set

	return knapsack, best_weight, best_value

# ============================================================
# 						     GREEDY - WEIGHT
# ============================================================

def greedy_solution(W, T):
    knapsack = []
    knapsack_weight = 0
    knapsack_value = 0

    items_sorted = sorted(T, key=weight, reverse=True)

    # print "\nSORTED-WEIGHT: ", items_sorted

    while len(items_sorted) > 0:
    	item = items_sorted.pop()
    	if weight(item) + knapsack_weight <= W:
    		knapsack.append(item)
    		knapsack_weight += weight(knapsack[-1])
    		knapsack_value += value(knapsack[-1])
    	else:
    		break

    return knapsack_value, len(knapsack), knapsack_weight

# ============================================================
# 						     GREEDY - VALUE
# ============================================================

# for greedy solution
def weight(task):
	return task[1]

def value(task):
	return task[2]

def greedy_solution_value(W, T):
    
    knapsack = []
    knapsack_weight = 0
    knapsack_value = 0

    items_sorted = sorted(T, key=value, reverse=True)

    while len(items_sorted) > 0:
    	item = items_sorted.pop()
    	if weight(item) + knapsack_weight <= W:
    		knapsack.append(item)
    		knapsack_weight += weight(knapsack[-1])
    		knapsack_value += value(knapsack[-1])
    	else:
    		break

    return knapsack_value, len(knapsack), knapsack_weight

# ============================================================
# 							DP
# ============================================================

def dp_solution(W, wt, val):
	result = []
	result1 = 0
	n = len(val)
	K = [[0 for x in range(W + 1)] for x in range(n + 1)]
	print ("variaveis W, wt e val, recebidas: ", W, wt, val )
	#print ("K: ", K)
	# Build table K[][] in bottom up manner
	for i in range(n + 1):
		for w in range(W + 1):
			# base case
			if i == 0 or w == 0:
				K[i][w] = 0
			elif wt[i-1] <= w:
				K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
			else:
				K[i][w] = K[i-1][w]

	# stores the result of Knapsack
	res = K[n][W]

   	#print ("res ", res)

	w = W
	for i in range(n, 0, -1): 
		if res <= 0:
			break

		if res == K[i - 1][w]:
			continue
		else:
			# This item is included. 
			#print ("item incluido")
			#print (i-1, wt[i-1], val[i-1])
			result.append((i-1, wt[i-1], val[i-1]))
			result1 += wt[i-1]
			# Since this weight is included 
			# its value is deducted 
			res = res - val[i - 1] 
			w = w - wt[i - 1]

	#print ("retorno: ", K[n][W], len(result), result1)
	# return K[n][W], len(result), result
	return K[n][W], len(result), result1

# ============================================================
# 						DP-MORS
# ============================================================

def dp_solution_mors(W, wt, val):
	result = []
	result1 = 0
	n = len(val)
	K = [[0 for x in range(W + 1)] for x in range(n + 1)]
	
	print ("DP solution")
	print ("W ", W )
	print ("wt ", wt)
	print ("val ", val)
	#print ("K ", K)
	# Build table K[][] in bottom up manner
	for i in range(n + 1):
		for w in range(W + 1):
			# base case
			if i == 0 or w == 0:
				K[i][w] = 0
			elif wt[i-1] <= w:
				K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
			else:
				K[i][w] = K[i-1][w]

	# stores the result of Knapsack
	res = K[n][W]
	print (res)
   	# print res

	w = W
	for i in range(n, 0, -1): 
		if res <= 0:
			break

		if res == K[i - 1][w]:
			continue
		else:
			# This item is included. 
			# print i-1, wt[i-1], val[i-1]
			result.append([i-1, wt[i-1], val[i-1]])
			result1 += wt[i-1]
			print ("result1: ", result1)
			# Since this weight is included 
			# its value is deducted 
			res = res - val[i - 1] 
			w = w - wt[i - 1]

	# return K[n][W], len(result), result
	return K[n][W], len(result), result, result1

# ============================================================
# 						     GREEDY - WEIGHT - MORS
# ============================================================

def greedy_solution_mors(W, T):
    
    knapsack = []
    knapsack_weight = 0
    knapsack_value = 0

    items_sorted = sorted(T, key=weight, reverse=True)

    # print "\nSORTED-WEIGHT: ", items_sorted

    while len(items_sorted) > 0:
    	item = items_sorted.pop()
    	if weight(item) + knapsack_weight <= W:
    		knapsack.append(item)
    		knapsack_weight += weight(knapsack[-1])
    		knapsack_value += value(knapsack[-1])
    	else:
    		break

    return knapsack_value, len(knapsack), knapsack, knapsack_weight

# ============================================================
# 							GREEDY-MORS
# ============================================================

def greedy_mors(W, T, sorted_vccs):
	print("Clusters: ",W)
	vi = 0

	bloqueio = 0
	atendimento = 0
	tempo = 0.0

	gain_mors = 0
	alocadas = 0
	nao_alocadas = 0

	VCC = []
	for j,k in W.items():
		VCC.append(k)

	if sorted_vccs == True:
		VCC = sorted(VCC, reverse=True)

	# print "\nVCC:",VCC
	
	# cont_vi = 0
	cont_peso = 0

	while len(T) > 0:
		# cont += 1
		# print len(T)
		# print  "\nT inicial:",T
		if len(VCC) > 0:
			# print cont, " Ha espaco na VCC"
			# atendimento += 1
			vi = VCC.pop(0)

			# DP solution usage
			valor, tarefas_alocadas, t_restante, peso = greedy_solution_mors(vi, T)
			
			gain_mors += valor
			alocadas += tarefas_alocadas
			# cont_vi += vi # removido pois nao era necessario
			cont_peso += peso

			# Atualiza T
			for k in t_restante:
				if k in T:
					T.remove(k)

			# atribui novo indice para cada tarefa
			for k in range(len(T)):
				T[k][0] = k

			# print "Tarefas alocadas:", sorted(t_restante)
			# print "Novo T:", sorted(T)

			if len(T) == 0:
				# print len(T)
				# print "Sem tarefas!"
				break

		else:
			# bloqueio += 1
			# print "VCC vazia!"
			nao_alocadas = len(T)
			break

	# print "FIM do MORS"
	# return gain_mors, alocadas, cont_vi, cont_peso
	return gain_mors, alocadas, cont_peso

# ============================================================
# 							MORS
# ============================================================

def mors(W, T, sorted_vccs):
	#edicao douglas
	print (W)
	print (T)
	print (sorted_vccs)
	W = {0: 20,1:30,2:60}
	vi = 0

	bloqueio = 0
	atendimento = 0
	tempo = 0.0

	gain_mors = 0
	alocadas = 0
	nao_alocadas = 0

	VCC = []
	for j,k in W.items():
		VCC.append(k)

	if sorted_vccs == True:
		VCC = sorted(VCC, reverse=True)

	print ("\nVCC: ",VCC)
	
	# cont_vi = 0
	cont_peso = 0

	while len(T) > 0:
		# cont += 1
		# print len(T)
		# print  "\nT inicial:",T
		if len(VCC) > 0:
			# print cont, " Ha espaco na VCC"
			# atendimento += 1
			vi = VCC.pop(0)

			# for DP solution
			wt = []
			T1 = []
			for i in T:
				wt.append(i[1])
				T1.append(i[2])
			
			print ("wt ",wt)
			print ("t1 ", T1)
			# DP solution usage
			valor, tarefas_alocadas, t_restante, peso = dp_solution_mors(vi, wt, T1)
			print ("valor ",valor)
			print ("tarefa ",tarefas_alocadas)
			print ("restante ",t_restante)
			gain_mors += valor
			alocadas += tarefas_alocadas
			# cont_vi += vi # removido pois nao era necessario
			cont_peso += peso

			# Atualiza T
			for k in t_restante:
				if k in T:
					T.remove(k)

			# atribui novo indice para cada tarefa
			for k in range(len(T)):
				T[k][0] = k

			# print "Tarefas alocadas:", sorted(t_restante)
			# print "Novo T:", sorted(T)

			if len(T) == 0:
				# print len(T)
				# print "Sem tarefas!"
				break

		else:
			# bloqueio += 1
			# print "VCC vazia!"
			nao_alocadas = len(T)
			break
	
	print ("FIM do MORS")
	# return gain_mors, alocadas, cont_vi, cont_peso
	return gain_mors, alocadas, cont_peso
