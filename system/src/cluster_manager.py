#!/usr/bin/env python
# Joahannes B. D. da Costa <joahannes@lrc.ic.unicamp.br>

from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

from shapely.geometry import MultiPoint
from geopy.distance import great_circle

import pandas as pd
import numpy as np

import log_manager
import allocation_manager
import task_manager
import plot_manager

import traci

import networkx as nx
import math

# MANTER CLUSTERS NA MEMORIA
clusters_set = {}

def get_centermost_point(cluster):
	centroid = (MultiPoint(cluster).centroid.x, MultiPoint(cluster).centroid.y)
	centermost_point = min(cluster, key=lambda point: great_circle(point, centroid).m)
	return tuple(centermost_point)

def prepare_nodes(vehicles_list, delta_resource, delta_weight, radius, number_of_tasks, step):
	
	# print(" * [DEBUG] >> clusterizando...")
	file = open("veiculos.txt","a")
	file.write(str(vehicles_list)+"\n")
	veiculos = []
	for i in range(len(vehicles_list)):
		x = str(traci.vehicle.getPosition(vehicles_list[i])).split(",")
		x = str(x[0]).split("(")

		y = str(traci.vehicle.getPosition(vehicles_list[i])).split()
		y = str(y[1]).split(")")

		x = float(x[1])
		y = float(y[0])

		print(x)
		print(y)

		# veiculos[vehicles_list[i]] = x, y
		veiculos.append([vehicles_list[i], x, y]) # vehicles_list[i]
		#file.write(str(vehicles_list[i])+"\n")
		file.write(str(vehicles_list[i])+","+str(x)+","+str(y)+"\n")
	file.close()

	labels, core_samples_mask, n_clusters_, X = dbscan(veiculos, radius)

	# compute CHs
	centroids, clusters_map = get_clusters(X, labels, n_clusters_)

	# resources
	resource_per_cluster = get_resource_cluster(clusters_map, delta_resource)
	log_manager.log_resources(step, n_clusters_, resource_per_cluster, delta_resource, delta_weight, radius)
	
	# tasks 
	generate_tasks = task_manager.generate_task(number_of_tasks, delta_weight)
	log_manager.log_tasks(step, number_of_tasks, generate_tasks, delta_resource, delta_weight, radius)

	# for PLI log
	# if step == 504:
	# log_manager.log_pli(step, generate_tasks, resource_per_cluster)
	
	# allocation
	allocation_manager.task_allocation(step, resource_per_cluster, generate_tasks)

	# plot for debug
	# plot_manager.plot_cluster(labels, core_samples_mask, n_clusters_, radius, X, step, rep_points)
	# plot_manager.plot_clusters(veiculos, clusters_map, labels, radius, step, centroids, noise_map)

def dbscan(file, radius):
	# pandas dataframe
	# a = id_sumo, x, y
	a = np.array(file)
	# pega apenas x e y para clusterizar
	X = a[:,1:3]
	X = StandardScaler().fit_transform(X)
	
	# compute DBSCAN
	db = DBSCAN(eps=radius, min_samples=2).fit(X)
	core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
	core_samples_mask[db.core_sample_indices_] = True

	labels = db.labels_
	n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
	# n_noise_ = list(labels).count(-1)

	return labels, core_samples_mask, n_clusters_, X

def get_clusters(X, labels, n_clusters_):

	clusters = pd.Series([X[labels == n] for n in range(n_clusters_)])

	cluster_dict = {i: X[labels == i] for i in range(n_clusters_)}

	centermost_points = clusters.map(get_centermost_point)
	x, y = zip(*centermost_points)
	rep_points = pd.DataFrame({'x':x,'y':y})

	return rep_points, cluster_dict

def get_resource_cluster(cluster_dict, delta_resource):
	
	resource = {}
	for i in cluster_dict:
		resource[i] = (len(cluster_dict[i]) - 1) * delta_resource
	
	# print "Resources:", resource
	return resource
