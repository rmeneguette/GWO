#!/usr/bin/env python
# Joahannes B. D. da Costa <joahannes@lrc.ic.unicamp.br>

import matplotlib.pyplot as plt
import numpy as np

import imageio

# for graphs
import networkx as nx
# import community

def plot_cluster(labels, core_samples_mask, n_clusters_, radius, X, step, centroids):
	# print vehicles

	unique_labels = set(labels)

	colors = [plt.cm.Spectral(each)
		for each in np.linspace(0, 1, len(unique_labels))
	]

	for k, col in zip(unique_labels, colors):
		if k == -1:
			# Black used for noise.
			col = [0, 0, 0, 1]

		class_member_mask = (labels == k)

		xy = X[class_member_mask & core_samples_mask]
		plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col), markeredgecolor='k', markersize=6)

		xy = X[class_member_mask & ~core_samples_mask]
		plt.plot(xy[:, 0], xy[:, 1], 's', markerfacecolor=tuple(col), markeredgecolor='k', markersize=2)

	# plot centroids
	plt.plot(centroids['x'], centroids['y'], 'x', c = 'red', markersize=3)

	# plt.axis('off')
	
	# plt.ylim(-1000, 4)
	# plt.xlim(-1000, 4)

	plt.title(' DBSCAN - %ds \n Clusters: %d / Raio: %dm' % (step, n_clusters_, (radius*1000)))
	name = 'images/cluster_dbscan1_'+str(step)+'.png'
	plt.savefig(name)
	plt.close()

def plot_clusters(vehicles, clusters_map, labels, radius, step, centroids, noise_map):
	
	colors = [plt.cm.Spectral(each)
		for each in np.linspace(0, 1, len(clusters_map))
	]

	img = imageio.imread('/home/joahannes/projeto/vcc-centralized/vcc-centralized/scenario/lust/cenario.png')

	for k, col in zip(range(len(clusters_map)), colors):
		# PLOT VEICULOS NO CLUSTER
		for i in clusters_map[k]:
			for j in vehicles:
				if i == j[0]:
					plt.plot(j[1], j[2], 'o', markerfacecolor=tuple(col), markeredgecolor='k', markersize=6)
		
		# PLOT CLUSTER HEADS
		for i in centroids[k]:
			for j in vehicles:
				if i == j[0]:
					plt.plot(j[1], j[2], 'x', c='red', markeredgecolor='k', markersize=4)

		# PLOT RUIDO
		for i in noise_map:
			for j in vehicles:
				if i in j[0]:
					plt.plot(j[1], j[2], 's', markerfacecolor=tuple([0, 0, 0, 1]), markeredgecolor='k', markersize=2)

	plt.axis('on')

	x_lim = 14000
	y_lim = 12000
	
	plt.xlim(0, x_lim)
	plt.ylim(0, y_lim)

	plt.imshow(img, alpha=0.5, zorder=0, extent=[0, x_lim, 0, y_lim])

	plt.title(' DBSCAN - %ds \n Clusters: %d / Raio: %dm' % (step, len(clusters_map), (radius*1000)))
	name = 'images/cluster_dbscan2_'+str(step)+'.png'
	plt.savefig(name, dpi=200)
	plt.close()

def plot_graph(G, positions, step):

	img = imageio.imread('/home/joahannes/projeto/vcc-centralized/vcc-centralized/scenario/lust/cenario.png')

	plt.axis('on')
	
	x_lim = 14000
	y_lim = 12000
	
	plt.xlim(0, x_lim)
	plt.ylim(0, y_lim)

	plt.imshow(img, alpha=0.5, extent=[0, x_lim, 0, y_lim])
	
	nx.draw_networkx(
		G,
		pos = positions,
		# cmap = plt.get_cmap("jet"),
		# # node_color = values,
		node_size = 20,
		edge_color = 'k',
		with_labels = False
	)

	# fig = plt.figure()
	ax = plt.gca() # to get the current axis
	fig = plt.gcf()
	ax.collections[0].set_edgecolor("#000000")

	plt.title("LuST Scenario "+str(step)+" s")

	fig.savefig('social'+str(step)+'.png', dpi=150, bbox_inches = 'tight', pad_inches = 0.04, transparent=False)
	plt.close()
