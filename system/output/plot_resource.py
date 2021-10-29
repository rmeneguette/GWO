# -*- coding: UTF-8 -*-

# File name: plot_allocation.py
# Author: Joahannes Costa
# Data create: 12/09/2019

from __future__ import division
import math
import matplotlib.pyplot as plt
import numpy as np

# instancias para o plot
TAMANHO = (1, 5, 10, 15, 20)

# identificacao dos algoritmos
ALGORITHM = (0, 1, 4, 6)

HATCHS = {0 : '', 1 : '', 2 : '', 4 : ''} #

x_tam = 5
y_tam = 5

# configuracoes de estilo
LABEL = {
	0: "GREEDY",  #0 : "GREEDY-1",
	1 : "DP",
	4 : "GREEDY-N",
	6: "GTA"
}

MARKS = {
	0 : "s",#"GREEDY",  #0 : "GREEDY-1",
	1 : "o",#"DP",
	4 : "v",#3"GREEDY-N",
	6 : "s",#"BAT",
}

LINES = {
	0 : "--",
	1 : "-",
	4 : ":",
	6 : "-."
}

COLORS = {
	0 : "red", 
	1 : "blue",
	4 : "green",
	6 : "orange"
}

markersize = 6
linewidth = 3

capsize = 0

formato = '.eps'
legenda_size = 18
legenda_algoritmos = 14.5

cenario_raio = '100'
recursos = '3'

# 24h 		= 0, 87480
# 6h-9h 	= 21600, 32400
# 14h-16h	= 50400, 57600
tinicio = 0
tfim = 200

#CONFIDENCE INTERVAL - BAR ERROR
def confidence_interval(values):
	N = len(values)
	Z = 1.96
	std_dev = np.std(values)
	std_error = std_dev / math.sqrt(N)
	return Z * std_error
	
def plot_alocacao_ganho():

	print ("\nGANHO: ")

	for algorithm in ALGORITHM:

		print(LABEL[algorithm],)
		
		gain_values = []
		confidence_intervals = []

		for tamanho in TAMANHO:
			
			values = []
			gain = 0

			# 0 tempo 1 vcc 2 tarefas 3 algoritmo 4 ganho 5 tarefas_alocadas
			file_input_name = 'allocation_'+str(cenario_raio)+'_'+str(recursos)+'_'+str(tamanho)+'.txt'

			for line in open(file_input_name):

				if int(line.split()[0]) > tinicio and int(line.split()[0]) < tfim:

					if int(line.split()[3]) == algorithm:
						gain = int(line.split()[4])
					
					values.append(gain)

			gain_values.append(np.mean(values))
			confidence_intervals.append(confidence_interval(values))

		print(gain_values)
		
		plt.errorbar(
			TAMANHO,
			gain_values,
			yerr = confidence_intervals,
			label = LABEL[algorithm],
			marker=MARKS[algorithm],
			linestyle=LINES[algorithm],
			markersize = markersize,
			linewidth = linewidth,
			color=COLORS[algorithm],
			capsize = capsize,
			markeredgecolor = "k",
			markeredgewidth = 0.5)
		
	plt.grid(color='0.9', linestyle='--', linewidth=0.4, axis='both', alpha=0.1)

	plt.legend(
		numpoints 	= 1,
		loc 		= 2,
		fancybox 	= False,
		# frameon 	= True,
		shadow		= False,
		borderpad	= 0.4,
		framealpha	= 1,
		edgecolor	= 'k',
		fontsize 	= legenda_algoritmos
		)
	fig = plt.gcf()

	# plt.title(recursos+'r - '+cenario_raio+'m', fontsize=legenda_size)
	# plt.ylim(-100, 1601, 400)
	# yticks = np.arange(0, 1601, 400)

	plt.yticks(fontsize=legenda_size)
	plt.xticks(TAMANHO, fontsize=legenda_size)
	plt.ylabel('Ganho (#)', fontsize=legenda_size)
	plt.xlabel('Peso das tarefas', fontsize=legenda_size)

	fig.savefig('allocation_gain_'+cenario_raio+'_'+recursos+formato, dpi=200, bbox_inches = 'tight', pad_inches = 0.05)
	
	plt.close()

def plot_alocacao_eficiencia():

	print("\nATENDIMENTO: ")

	for algorithm in ALGORITHM:
		
		print(LABEL[algorithm],)

		number_values = []
		confidence_intervals = []

		for tamanho in TAMANHO:
	
			values = []
			number = 1

			# 0 tempo 1 vcc 2 tarefas 3 algoritmo 4 ganho 5 tarefas_alocadas
			file_input_name = 'allocation_'+str(cenario_raio)+'_'+str(recursos)+'_'+str(tamanho)+'.txt'

			for line in open(file_input_name):
				
				if int(line.split()[0]) > tinicio and int(line.split()[0]) < tfim:
					
					if int(line.split()[3]) == algorithm:
						
						if int(line.split()[2]) > 0:
							number = (int(line.split()[5]) * 100) / int(line.split()[2])
					
					values.append(number)

			values = np.divide(values, 1)

			number_values.append(np.mean(values))
			confidence_intervals.append(confidence_interval(values))

		print(number_values)
		
		plt.errorbar(
			TAMANHO,
			number_values,
			yerr = confidence_intervals,
			label = LABEL[algorithm],
			marker=MARKS[algorithm],
			linestyle=LINES[algorithm],
			markersize = markersize,
			linewidth = linewidth,
			color=COLORS[algorithm],
			capsize = capsize,
			markeredgecolor = "k",
			markeredgewidth = 0.5)

	plt.grid(color='0.9', linestyle='--', linewidth=0.4, axis='both', alpha=0.1)

	plt.legend(
		numpoints 	= 1,
		loc 		= 3,
		fancybox 	= False,
		# frameon 	= True,
		shadow		= False,
		borderpad	= 0.4,
		framealpha	= 1,
		edgecolor	= 'k',
		fontsize 	= legenda_algoritmos
		)
	fig = plt.gcf()

	# plt.ylim(45, 103, 10)
	# plt.title(recursos+'r - '+cenario_raio+'m', fontsize=legenda_size)

	plt.yticks(fontsize=legenda_size)
	plt.xticks(TAMANHO, fontsize=legenda_size)
	plt.ylabel('Tarefas alocadas (%)', fontsize=legenda_size)
	plt.xlabel('Peso das tarefas', fontsize=legenda_size)

	fig.savefig('allocation_efficiency_'+cenario_raio+'_'+recursos+formato, dpi=200, bbox_inches = 'tight', pad_inches = 0.05)
	
	plt.close()


def plot_utilizacao():

	print("\nUTILIZACAO:")

	for algorithm in ALGORITHM:

		print(LABEL[algorithm],) 
		
		number_values = []
		confidence_intervals = []

		number = 0

		for tamanho in TAMANHO:
			
			values = []
			
			# 0 tempo 1 vcc 2 tarefas 3 algoritmo 4 ganho 5 tarefas_alocadas
			file_input_name = 'allocation_'+str(cenario_raio)+'_'+str(recursos)+'_'+str(tamanho)+'.txt'

			for line in open(file_input_name):

				if int(line.split()[0]) > tinicio and int(line.split()[0]) < tfim:
					
					if int(line.split()[3]) == algorithm:
						if int(line.split()[1]) > 0:

							number = (int(line.split()[7]) * 100) / (int(line.split()[1]))

					values.append(number)

			values = np.divide(values, 1)

			number_values.append(np.mean(values))
			confidence_intervals.append(confidence_interval(values))
		
		print(number_values)

		plt.errorbar(
			TAMANHO,
			number_values,
			yerr = confidence_intervals,
			label = LABEL[algorithm],
			marker=MARKS[algorithm],
			linestyle=LINES[algorithm],
			markersize = markersize,
			linewidth = linewidth,
			color=COLORS[algorithm],
			capsize = capsize,
			markeredgecolor = "k",
			markeredgewidth = 0.5)

	plt.grid(color='0.9', linestyle='--', linewidth=0.4, axis='both', alpha=0.1)

	plt.legend(
		numpoints 	= 1,
		loc 		= 4,
		fancybox 	= False,
		# frameon 	= True,
		shadow		= False,
		borderpad	= 0.4,
		framealpha	= 1,
		edgecolor	= 'k',
		fontsize 	= legenda_algoritmos
		)
	fig = plt.gcf()

	# plt.title(recursos+'r - '+cenario_raio+'m', fontsize=legenda_size)
	plt.ylim(-2, 61.5, 10)

	plt.yticks(fontsize=legenda_size)
	plt.xticks(TAMANHO, fontsize=legenda_size)
	plt.ylabel('Utilizacao dos recursos (%)', fontsize=legenda_size)
	plt.xlabel('Peso das tarefas', fontsize=legenda_size)

	fig.savefig('allocation_utilization_'+cenario_raio+'_'+recursos+formato, dpi=200, bbox_inches = 'tight', pad_inches = 0.05)
	
	plt.close()

def plot_cpu_time():

	print ("\nCPU_TIME:")

	for algorithm in ALGORITHM:

		print (LABEL[algorithm])

		gain_values = []
		gain_values_pli = []
		confidence_intervals = []
		confidence_intervals_pli = []

		for tamanho in TAMANHO:
			
			values = []
			values_pli = []
			gain = 0
			
			# 0 tempo 1 vcc 2 tarefas 3 algoritmo 4 ganho 5 tarefas_alocadas
			file_input_name = 'allocation_'+str(cenario_raio)+'_'+str(recursos)+'_'+str(tamanho)+'.txt'
			#file_input_pli = 'result_final_'+str(recursos)+'.txt'

			for line in open(file_input_name):

				if int(line.split()[0]) > tinicio and int(line.split()[0]) < tfim:

					if int(line.split()[3]) == algorithm:
						gain = float(line.split()[8])

					values.append(gain)

			#for line in open(file_input_pli):

			#	if int(line.split()[0]) > tinicio and int(line.split()[0]) < tfim:

			#		if int(line.split()[3]) == algorithm:
						# print int(line.split()[4])
			#			gain += float(line.split()[8])

			#		values_pli.append(gain)
			
			gain_values.append(np.mean(values))
			#gain_values_pli.append(np.mean(values_pli))
			confidence_intervals.append(confidence_interval(values))
			#confidence_intervals_pli.append(confidence_interval(values_pli))

		print (gain_values)

		x = np.arange(len(TAMANHO))		
		ax = plt.subplot()

		width = 0.28
		
		if(algorithm == 0):
			ax.bar(x - width, gain_values, align='center', yerr=confidence_intervals, color=COLORS[algorithm], width=width, hatch=HATCHS[algorithm], label=LABEL[algorithm], edgecolor='k', error_kw=dict(elinewidth=1, capsize = 2, ecolor='black'))

		if(algorithm == 4):
			ax.bar(x, gain_values, align='center', yerr=confidence_intervals, color=COLORS[algorithm], width=width, hatch=HATCHS[algorithm], label=LABEL[algorithm], edgecolor='k', error_kw=dict(elinewidth=1, capsize = 2,ecolor='black'))

		if(algorithm == 2):
			ax.bar(x + width, gain_values, align='center', yerr=confidence_intervals, color=COLORS[algorithm], width=width, hatch=HATCHS[algorithm], label=LABEL[algorithm], edgecolor='k', error_kw=dict(elinewidth=1, capsize = 2, ecolor='black'))

		if (algorithm == 1):
			ax.bar(x + width, gain_values, align='center', yerr=confidence_intervals, color=COLORS[algorithm],
				   width=width, hatch=HATCHS[algorithm], label=LABEL[algorithm], edgecolor='k',
				   error_kw=dict(elinewidth=1, capsize=2, ecolor='black'))

	ax.legend(
		numpoints 	= 1,
		loc 		= 'upper center',
		bbox_to_anchor=(-0.025, 0.63, 1.055, 0.5),
		ncol		= 3,
		fancybox 	= False,
		frameon 	= True,
		shadow		= False,
		# borderpad	= 2,
		mode		= "expand",
		edgecolor	= 'k',
		fontsize 	= legenda_size
		)

	ax.set_ylabel(r"CPU time (s)", fontsize=legenda_size)
	ax.set_xlabel(u"Resources (#)", fontsize=legenda_size)

	# We change the fontsize of minor ticks label 
	ax.tick_params(axis='both', which='major', labelsize=legenda_size)
	ax.tick_params(axis='both', which='minor', labelsize=legenda_size)

	ax.set_xticks(x)
	ax.set_xticklabels(TAMANHO, fontsize=legenda_size)

	ax.set_axisbelow(True)

	# ax.set_ylim(0, 5000)

	ax.set_yscale('log')

	# plt.title(r'$\mu$ = '+str(tamanho), fontsize=legenda_size)

	plt.grid(color='0.85', linestyle='--', linewidth=0.5, axis='both', alpha=0.1)
	
	fig = plt.gcf()
	fig.set_size_inches(x_tam, y_tam)
	fig.savefig('1706_cputime_barra_'+str(tamanho)+formato, dpi=200, bbox_inches = 'tight', pad_inches = 0.04 )

	plt.close()


if __name__ == "__main__":

	plot_alocacao_ganho()
	plot_alocacao_eficiencia()
	plot_utilizacao()
	plot_cpu_time()