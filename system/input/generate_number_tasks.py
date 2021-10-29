#!/usr/bin/env python

import numpy as np
import random

from scipy.stats import poisson

import matplotlib.pyplot as plt

def generate_number_of_tasks(plot):
	# TESTE 2
	# compute poisson
	poisson_set = compute_poisson()

	# cria arquivo de distribuicao das tarefas
	teste_file = open('teste_TASKS.txt','w')
	# poisson_set.sort()
	for i in poisson_set:
		teste_file.write(str(i) + "\n")
	teste_file.close()
	
	if plot == True:
		# descomentar para visualizar o plot da poisson
		count, bins, ignored = plt.hist(
			poisson_set,
			# ,
			facecolor='red',
			edgecolor='black',
			density=True,
			align='mid',
			alpha=0.7)
		plt.xlabel('Number of tasks')
		plt.ylabel(r'$P(X = k) = \frac{e^{-k} . \lambda^k}{k!}$')
		# plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
		plt.savefig('tasks_arrival.eps', dpi=200, bbox_inches = 'tight', pad_inches = 0.05)
		plt.close()

def compute_poisson():
	lamb = 20 # esperanca de ocorrencia
	size = 2000
	s = np.random.poisson(lamb,size)

	return s

def plot_poisson():

	PROB = (1,5,10,15,20)
	STYLE = {1:"-", 5:"-.", 10:"-", 15:":", 20:"--"}

	# TESTE 1
	arr = []
	for i in PROB:
		rv = poisson(i)
		for num in range(0,40):
	 		arr.append(rv.pmf(num))

		prob = rv.pmf(i)

		plt.xlabel('Number of tasks')
		plt.ylabel(r'$P(X = k) = \frac{e^{-k} . \lambda^k}{k!}$')

		# plt.grid(True)
		plt.plot(arr, linewidth=1.5, linestyle=STYLE[i], label=r'$\lambda = $'+str(i))
		plt.plot([i], [prob], marker='o', markersize=6, color="red")

		arr = []

	plt.legend()

	plt.savefig('tasks_arrival_TESTE.eps', dpi=400, bbox_inches = 'tight', pad_inches = 0.05)

	plt.close()
	
if __name__ == "__main__":

	# plot_poisson()
	generate_number_of_tasks(True)