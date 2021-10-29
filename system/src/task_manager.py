#!/usr/bin/env python
# Joahannes B. D. da Costa <joahannes@lrc.ic.unicamp.br>

import random
import log_manager

import numpy as np

# lixo, tirar depois
def compute_poisson():
	lem = 20
	size = 10000
	s = np.random.poisson(lem,size)

	return s

def generate_task(task_n, weight):

	# print "Number of tasks:", task_n
	# tasks = {} # dicionario
	tasks = []

	for i in range(task_n):
		# task_x = 0.0
		# task_y = 0.0
		# task_deadline = random.randint(1,i+2)
		task_weight = random.randint(1,weight*2)
		task_value = random.randint(2,task_weight*2)

		tasks.append([i, task_weight, task_value]) # mudei de () para []
		# tasks[i] = task_deadline, task_weight, task_value # dicionario

	# print "Tasks generated:", tasks

	return tasks

def load_number_of_tasks():

	tasks_file = 'input/number_of_tasks.txt'
	
	tasks_set = []

	for i in open(tasks_file):
		tasks_set.append(int(i.split()[0]))

	return tasks_set
