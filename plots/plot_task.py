# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt

LABEL = {
	0 : "GREEDY",  
	1 : "DP",
	4 : "GREEDY-N",
	6 : "BAT",
}


def graf_recompensa():
	dados_Greedy = [1.3, 2.3, 3.8]
	dados_GreedyN = [1.8, 3.5, 5.3]
	dados_DP = [1.2, 2.1, 3.6]
	dados_BAT = [2.2, 4.3, 10]

	erro_margem_Greedy = [0.3, 0.3, 0.4]
	erro_margem_GreedyN = [0.4, 0.2, 0.3]
	erro_margem_DP = [0.2, 0.2, 0.3]
	erro_margem_BAT = [0.2, 0.3, 0.5]

	barWidth = 0.20

	plt.figure(figsize=(310,25))

	r1 = np.arange(len(dados_Greedy))
	r2 = [x + barWidth for x in r1]
	r3 = [x + barWidth for x in r2]
	r4 = [x + barWidth for x in r3]


	plt.bar(r1, dados_Greedy, color="aquamarine", width=barWidth, label="Greedy", yerr=erro_margem_Greedy)
	plt.bar(r2, dados_GreedyN, color="turquoise", width=barWidth, label="Greedy-N",yerr=erro_margem_GreedyN)
	plt.bar(r3, dados_DP, color="slateblue", width=barWidth, label="DP",yerr=erro_margem_DP)
	plt.bar(r4, dados_BAT, color="blueviolet", width=barWidth, label="ARCANE",yerr=erro_margem_BAT)



	plt.legend(loc='best', fontsize=14)
	plt.xlabel("Recursos (#)")
	plt.xticks([r + barWidth for r in range(len(dados_Greedy))],["1","2","3","4"])
	plt.ylabel("Recompensa (#)")

	plt.show()

def graf_atendimento():
	dados_Greedy = [3.6, 6.3, 9.8]
	dados_GreedyN = [5.3, 10.0, 14]
	dados_DP = [3.3, 5.9, 8.9]
	dados_BAT = [6.4, 12.2, 18.2]

	erro_margem_Greedy = [0.3, 0.4, 0.4]
	erro_margem_GreedyN = [0.3, 0.4, 0.8]
	erro_margem_DP = [0.3, 0.4, 0.4]
	erro_margem_BAT = [0.4, 0.8, 1.0]

	barWidth = 0.20

	plt.figure(figsize=(310,25))

	r1 = np.arange(len(dados_Greedy))
	r2 = [x + barWidth for x in r1]
	r3 = [x + barWidth for x in r2]
	r4 = [x + barWidth for x in r3]


	plt.bar(r1, dados_Greedy, color="aquamarine", width=barWidth, label="Greedy", yerr=erro_margem_Greedy)
	plt.bar(r2, dados_GreedyN, color="turquoise", width=barWidth, label="Greedy-N",yerr=erro_margem_GreedyN)
	plt.bar(r3, dados_DP, color="slateblue", width=barWidth, label="DP",yerr=erro_margem_DP)
	plt.bar(r4, dados_BAT, color="blueviolet", width=barWidth, label="ARCANE",yerr=erro_margem_BAT)



	plt.legend(loc='best', fontsize=14)
	plt.xlabel("Recursos (#)")
	plt.xticks([r + barWidth for r in range(len(dados_Greedy))],["1","2","3","4"])
	plt.ylabel("Atendimento (%)")

	plt.show()


def graf_utilizacao():
	dados_Greedy = [16.6, 13.8, 16.6]
	dados_GreedyN = [41.6, 40.2, 42.7]
	dados_DP = [16.6, 15.2, 17.4]
	dados_BAT = [41.6, 40.2, 43]

	erro_margem_Greedy = [0.6, 0.8, 0.6]
	erro_margem_GreedyN = [0.6, 0.8, 0.8]
	erro_margem_DP = [0.6, 0.4, 0.8]
	erro_margem_BAT = [0.6, 0.8, 0.7]

	barWidth = 0.15

	plt.figure(figsize=(310,25))

	r1 = np.arange(len(dados_Greedy))
	r2 = [x + barWidth for x in r1]
	r3 = [x + barWidth for x in r2]
	r4 = [x + barWidth for x in r3]


	plt.bar(r1, dados_Greedy, color="aquamarine", width=barWidth, label="Greedy", yerr=erro_margem_Greedy)
	plt.bar(r2, dados_GreedyN, color="turquoise", width=barWidth, label="Greedy-N",yerr=erro_margem_GreedyN)
	plt.bar(r3, dados_DP, color="slateblue", width=barWidth, label="DP",yerr=erro_margem_DP)
	plt.bar(r4, dados_BAT, color="blueviolet", width=barWidth, label="ARCANE",yerr=erro_margem_BAT)

	#plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), mode="expand", loc="3", ncol="4", borderaxespad="0.")
	plt.legend(loc='best', fontsize=7.5)
	plt.xlabel("Recursos (#)")
	plt.xticks([r + barWidth for r in range(len(dados_Greedy))],["1","2","3","4"])
	plt.ylabel("Utilizacao (%)")

	plt.show()

def graf_cpu():
	dados_Greedy = [2.1, 2.2, 2.1]
	dados_GreedyN = [3.3, 3.7, 4.0]
	dados_DP = [5.3, 5.9, 7.1]
	dados_BAT = [0.5, 0.7, 0.6]

	erro_margem_Greedy = [0.1, 0.2, 0.1]
	erro_margem_GreedyN = [0.3, 0.4, 0.4]
	erro_margem_DP = [0.3, 0.4, 0.4]
	erro_margem_BAT = [0.1, 0.2, 0.15]

	barWidth = 0.20

	plt.figure(figsize=(310,25))

	r1 = np.arange(len(dados_Greedy))
	r2 = [x + barWidth for x in r1]
	r3 = [x + barWidth for x in r2]
	r4 = [x + barWidth for x in r3]


	plt.bar(r1, dados_Greedy, color="aquamarine", width=barWidth, label="Greedy", yerr=erro_margem_Greedy)
	plt.bar(r2, dados_GreedyN, color="turquoise", width=barWidth, label="Greedy-N",yerr=erro_margem_GreedyN)
	plt.bar(r3, dados_DP, color="slateblue", width=barWidth, label="DP",yerr=erro_margem_DP)
	plt.bar(r4, dados_BAT, color="blueviolet", width=barWidth, label="ARCANE",yerr=erro_margem_BAT)


	plt.legend(loc='best', fontsize=14)
	plt.xlabel("Recursos (#)")
	plt.xticks([r + barWidth for r in range(len(dados_Greedy))],["1","2","3","4"])
	plt.ylabel("Tempo de CPU (s)")

	plt.show()

graf_recompensa()
graf_atendimento()
graf_utilizacao()
graf_cpu()