#!/usr/bin/env python
# Joahannes B. D. da Costa <joahannes@lrc.ic.unicamp.br>

# LOG
#===============================================================#
# [0] step														#
# [1] recurso das vccs											#
# [2] numero de tarefas geradas									#
# [3] algoritmo utilizado: (0) guloso, (1) dp e (2) proposta	#
# [4] ganho por alocar as n tarefas								#
# [5] tarefas que foram alocadas								#
# [6] numero de vccs criadas									#
# [7] peso das tarefas											#
# [8] cpu_time													#
#===============================================================#

def get_informations(radius, resources, weight):
	
	global name	
	radius_log = int(radius*1000)
	global resource_log 
	resource_log = resources
	weight_log = weight
	name = 'output/allocation_'+str(radius_log)+'_'+str(resource_log)+'_'+str(weight_log)+'.txt'

def log_resources(step, number, resource_per_cluster, resource, weight, radius):
	resources_file = open('output/resources_'+str(radius)+'_'+str(resource)+'_'+str(weight)+'.txt','a')
	resources_file.write(str(step) + "," + str(number) + "," + str(resource_per_cluster) + "\n")
	resources_file.close()

	return resources_file

def log_tasks(step, number, tasks, resource, weight, radius):
	tasks_file = open('output/tasks_'+str(radius)+'_'+str(resource)+'_'+str(weight)+'.txt','a')
	tasks_file.write(str(step) + "," + str(number) + "," + str(tasks) + "\n")
	tasks_file.close()

	return tasks_file

def log_allocation(step, vcc_resource, n_tasks, algorithm, gain, tasks_allocated, n_vccs, n_peso, cpu_time):

	allocation_file = open(name,'a')
	allocation_file.write(
		str(step) + "\t" +
		str(vcc_resource) + "\t" +
		str(n_tasks) + "\t" +
		str(algorithm) + "\t" +
		str(gain) + "\t" +
		str(tasks_allocated) + "\t" +
		str(n_vccs) + "\t" +
		str(n_peso) + "\t" +
		str(cpu_time) + "\n"
		)
	allocation_file.close()

	return allocation_file

def log_pli(step, tarefas, nuvens):

	with open('output/pli_log'+str(resource_log)+'.txt', 'a') as f:
		f.write("step: " + str(step) + "\n")
		f.write(str(len(tarefas)) + " " + str(len(nuvens)) + "\n")
		for i in tarefas:
			f.write("%s " % i[1])
		f.write("\n")
		for j in tarefas:
			f.write("%s " % j[2])
		f.write("\n")
		for k,l in nuvens.items():
			f.write("%s " % l)
		f.write("\n\n")