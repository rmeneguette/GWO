# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt

LABEL = {
	0 : "GREEDY",  
	1 : "DP",
	4 : "GREEDY-N",
	6 : "GTA",
}


def graf_recompensa():
	dados1_Greedy = [2, 2, 2, 1, 1]
	dados1_DP = [1.75, 1.75, 1.75, 1, 1]
	dados1_GreedyN = [6, 4.5, 2.5, 3, 1]
	dados1_GTA = [4.5, 3.25, 2.25, 3, 1]

	erro1_margem_Greedy = [2 * 0.05, 2 * 0.05, 2 * 0.05, 1 * 0.05, 1 * 0.05]
	erro1_margem_DP = [1.75 * 0.05, 1.75 * 0.05, 1.75 * 0.05, 1 * 0.05, 1 * 0.05]
	erro1_margem_GreedyN = [6 * 0.05, 4.5 * 0.05, 2.5 * 0.05, 3 * 0.05, 1 * 0.05]
	erro1_margem_GTA = [4.5 * 0.05, 3.25 * 0.05, 2.25 * 0.05, 3 * 0.05, 1 * 0.05]

	dados2_Greedy = [4, 3, 3, 2, 2]
	dados2_DP = [3.5, 3.5, 3.5, 3, 1.5]
	dados2_GreedyN = [12, 9, 7, 5.5, 1]
	dados2_GTA = [9, 5.88, 5, 4, 0.5]

	erro2_margem_Greedy = [4 * 0.05, 3 * 0.05, 3 * 0.05, 2 * 0.05, 2 * 0.05]
	erro2_margem_DP = [3.5 * 0.05, 3.5 * 0.05, 3.5 * 0.05, 3 * 0.05, 1.5 * 0.05]
	erro2_margem_GreedyN = [12 * 0.05, 9 * 0.05, 7 * 0.05, 5.5 * 0.05, 1 * 0.05]
	erro2_margem_GTA = [9 * 0.05, 5.88 * 0.05, 5 * 0.05, 4 * 0.05, 0.5 * 0.05]

	dados3_Greedy = [6, 5, 5, 6, 2]
	dados3_DP = [5.25, 5.25, 4.75, 5.25, 1.75]
	dados3_GreedyN = [18, 12.5, 11, 9, 2]
	dados3_GTA = [13.5, 11.13, 8.25, 7.25, 1.5]

	erro3_margem_Greedy = [6 * 0.05, 5 * 0.05, 5 * 0.05, 6 * 0.05, 2 * 0.05]
	erro3_margem_DP = [5.25 * 0.05, 5.25 * 0.05, 4.75 * 0.05, 5.25 * 0.05, 1.75 * 0.05]
	erro3_margem_GreedyN = [18 * 0.05, 12.5 * 0.05, 11 * 0.05, 9 * 0.05, 2 * 0.05]
	erro3_margem_GTA = [13.5 * 0.05, 11.13 * 0.05, 8.25 * 0.05, 7.25 * 0.05, 1.5 * 0.05]

	barWidth = 0.20

	plt.figure(figsize=(31,25))

	r1 = np.arange(len(dados1_Greedy))
	r2 = [x + barWidth for x in r1]
	r3 = [x + barWidth for x in r2]
	r4 = [x + barWidth for x in r3]


	plt.bar(r1, dados1_Greedy, color="aquamarine", width=barWidth, label="Greedy", yerr=erro1_margem_Greedy)
	plt.bar(r2, dados1_DP, color="turquoise", width=barWidth, label="DP",yerr=erro1_margem_DP)
	plt.bar(r3, dados1_GreedyN, color="slateblue", width=barWidth, label="Greedy-N",yerr=erro1_margem_GreedyN)
	plt.bar(r4, dados1_GTA, color="blueviolet", width=barWidth, label="GTA",yerr=erro1_margem_GTA)


	plt.title("Recursos por veículo ω = 1", fontsize=50)
	plt.legend(loc='best', fontsize=40)
	plt.xlabel("Peso médio Tarefa (λ)", fontsize=50)
	plt.xticks([r + barWidth for r in range(len(dados1_Greedy))],["1","5","10","15","20"], fontsize=40)
	plt.ylabel("Recompensa (#)", fontsize=50)
	plt.yticks(fontsize=40)

	plt.savefig('ganho1.png')

	plt.figure(figsize=(31,25))

	r1 = np.arange(len(dados2_Greedy))
	r2 = [x + barWidth for x in r1]
	r3 = [x + barWidth for x in r2]
	r4 = [x + barWidth for x in r3]


	plt.bar(r1, dados2_Greedy, color="aquamarine", width=barWidth, label="Greedy", yerr=erro2_margem_Greedy)
	plt.bar(r2, dados2_DP, color="turquoise", width=barWidth, label="DP",yerr=erro2_margem_DP)
	plt.bar(r3, dados2_GreedyN, color="slateblue", width=barWidth, label="Greedy-N",yerr=erro2_margem_GreedyN)
	plt.bar(r4, dados2_GTA, color="blueviolet", width=barWidth, label="GTA",yerr=erro2_margem_GTA)


	plt.title("Recursos por veículo ω = 2", fontsize=50)
	plt.legend(loc='best', fontsize=40)
	plt.xlabel("Peso médio Tarefa (λ)", fontsize=50)
	plt.xticks([r + barWidth for r in range(len(dados2_Greedy))],["1","5","10","15","20"], fontsize=40)
	plt.ylabel("Recompensa (#)", fontsize=50)
	plt.yticks(fontsize=40)

	plt.savefig('ganho2.png')

	plt.figure(figsize=(31,25))

	r1 = np.arange(len(dados3_Greedy))
	r2 = [x + barWidth for x in r1]
	r3 = [x + barWidth for x in r2]
	r4 = [x + barWidth for x in r3]


	plt.bar(r1, dados3_Greedy, color="aquamarine", width=barWidth, label="Greedy", yerr=erro3_margem_Greedy)
	plt.bar(r2, dados3_DP, color="turquoise", width=barWidth, label="DP",yerr=erro3_margem_DP)
	plt.bar(r3, dados3_GreedyN, color="slateblue", width=barWidth, label="Greedy-N",yerr=erro3_margem_GreedyN)
	plt.bar(r4, dados3_GTA, color="blueviolet", width=barWidth, label="GTA",yerr=erro3_margem_GTA)


	plt.title("Recursos por veículo ω = 3", fontsize=50)
	plt.legend(loc='best', fontsize=40)
	plt.xlabel("Peso médio Tarefa (λ)", fontsize=50)
	plt.xticks([r + barWidth for r in range(len(dados3_Greedy))],["1","5","10","15","20"], fontsize=40)
	plt.ylabel("Recompensa (#)", fontsize=50)
	plt.yticks(fontsize=40)

	plt.savefig('ganho3.png')

def graf_atendimento():
	dados1_Greedy = [5.41, 5.41, 5.41, 2.78, 2.78]
	dados1_DP = [4.88, 4.88, 4.88, 2.9, 2.9]
	dados1_GreedyN = [16.48, 12.38, 7.12, 8.58, 3.03]
	dados1_GTA = [12.66, 9.22, 6.59, 8.71, 3.15]

	erro1_margem_Greedy = [5.41 * 0.05, 5.41 * 0.05, 5.41 * 0.05, 2.78 * 0.05, 2.78 * 0.05]
	erro1_margem_DP = [4.88 * 0.05, 4.88 * 0.05, 4.88 * 0.05, 2.9 * 0.05, 2.9 * 0.05]
	erro1_margem_GreedyN = [16.48 * 0.05, 12.38 * 0.05, 7.12 * 0.05, 8.58 * 0.05, 3.03 * 0.05]
	erro1_margem_GTA = [12.66 * 0.05, 9.22 * 0.05, 6.59 * 0.05, 8.71 * 0.05, 3.15 * 0.05]

	dados2_Greedy = [10.82, 8.04, 8.04, 5.41, 5.26]
	dados2_DP = [9.63, 6.85, 4.88, 4.88, 4.07]
	dados2_GreedyN = [32.71, 20.43, 12.38, 11.07, 2.88]
	dados2_GTA = [24.94, 12.66, 9.22, 8.56, 1.69]

	erro2_margem_Greedy = [10.82 * 0.05, 8.04 * 0.05, 8.04 * 0.05, 5.41 * 0.05, 5.26 * 0.05]
	erro2_margem_DP = [9.63 * 0.05, 6.85 * 0.05, 4.88 * 0.05, 4.88 * 0.05, 4.07 * 0.05]
	erro2_margem_GreedyN = [32.71 * 0.05, 20.43 * 0.05, 12.38 * 0.05, 11.07 * 0.05, 2.88 * 0.05]
	erro2_margem_GTA = [24.94 * 0.05, 12.66 * 0.05, 9.22 * 0.05, 8.56 * 0.05, 1.69 * 0.05]

	dados3_Greedy = [16.23, 13.6, 13.45, 13.45, 5.41]
	dados3_DP = [14.38, 7.65, 6.85, 11.6, 4.88]
	dados3_GreedyN = [48.93, 28.9, 19.26, 17.94, 5.66]
	dados3_GTA = [37.22, 13.97, 12.66, 14.78, 4.47]

	erro3_margem_Greedy = [16.23 * 0.05, 13.6 * 0.05, 13.45 * 0.05, 13.45 * 0.05, 5.41 * 0.05]
	erro3_margem_DP = [14.38 * 0.05, 7.65 * 0.05, 6.85 * 0.05, 11.6 * 0.05, 4.88 * 0.05]
	erro3_margem_GreedyN = [48.93 * 0.05, 28.9 * 0.05, 19.26 * 0.05, 17.94 * 0.05, 5.66 * 0.05]
	erro3_margem_GTA = [37.22 * 0.05, 13.97 * 0.05, 12.66 * 0.05, 14.78 * 0.05, 4.47 * 0.05]

	barWidth = 0.20

	plt.figure(figsize=(31,25))

	r1 = np.arange(len(dados1_Greedy))
	r2 = [x + barWidth for x in r1]
	r3 = [x + barWidth for x in r2]
	r4 = [x + barWidth for x in r3]


	plt.bar(r1, dados1_Greedy, color="aquamarine", width=barWidth, label="Greedy", yerr=erro1_margem_Greedy)
	plt.bar(r2, dados1_DP, color="turquoise", width=barWidth, label="DP",yerr=erro1_margem_DP)
	plt.bar(r3, dados1_GreedyN, color="slateblue", width=barWidth, label="Greedy-N",yerr=erro1_margem_GreedyN)
	plt.bar(r4, dados1_GTA, color="blueviolet", width=barWidth, label="GTA",yerr=erro1_margem_GTA)


	plt.title("Recursos por veículo ω = 1", fontsize=50)
	plt.legend(loc='best', fontsize=40)
	plt.xlabel("Peso médio Tarefa (λ)", fontsize=50)
	plt.xticks([r + barWidth for r in range(len(dados1_Greedy))],["1","5","10","15","20"], fontsize=40)
	plt.ylabel("Atendimento (%)", fontsize=50)
	plt.yticks(fontsize=40)

	plt.savefig("atendimento1.png")

	plt.figure(figsize=(31,25))

	r1 = np.arange(len(dados2_Greedy))
	r2 = [x + barWidth for x in r1]
	r3 = [x + barWidth for x in r2]
	r4 = [x + barWidth for x in r3]


	plt.bar(r1, dados2_Greedy, color="aquamarine", width=barWidth, label="Greedy", yerr=erro2_margem_Greedy)
	plt.bar(r2, dados2_DP, color="turquoise", width=barWidth, label="DP",yerr=erro2_margem_DP)
	plt.bar(r3, dados2_GreedyN, color="slateblue", width=barWidth, label="Greedy-N",yerr=erro2_margem_GreedyN)
	plt.bar(r4, dados2_GTA, color="blueviolet", width=barWidth, label="GTA",yerr=erro2_margem_GTA)


	plt.title("Recursos por veículo ω = 2", fontsize=50)
	plt.legend(loc='best', fontsize=40)
	plt.xlabel("Peso médio Tarefa (λ)", fontsize=50)
	plt.xticks([r + barWidth for r in range(len(dados2_Greedy))],["1","5","10","15","20"], fontsize=40)
	plt.ylabel("Atendimento (%)", fontsize=50)
	plt.yticks(fontsize=40)

	plt.savefig("atendimento2.png")

	plt.figure(figsize=(31,25))

	r1 = np.arange(len(dados3_Greedy))
	r2 = [x + barWidth for x in r1]
	r3 = [x + barWidth for x in r2]
	r4 = [x + barWidth for x in r3]


	plt.bar(r1, dados3_Greedy, color="aquamarine", width=barWidth, label="Greedy", yerr=erro3_margem_Greedy)
	plt.bar(r2, dados3_DP, color="turquoise", width=barWidth, label="DP",yerr=erro3_margem_DP)
	plt.bar(r3, dados3_GreedyN, color="slateblue", width=barWidth, label="Greedy-N",yerr=erro3_margem_GreedyN)
	plt.bar(r4, dados3_GTA, color="blueviolet", width=barWidth, label="GTA",yerr=erro3_margem_GTA)


	plt.title("Recursos por veículo ω = 3", fontsize=50)
	plt.legend(loc='best', fontsize=40)
	plt.xlabel("Peso médio Tarefa (λ)", fontsize=50)
	plt.xticks([r + barWidth for r in range(len(dados3_Greedy))],["1","5","10","15","20"], fontsize=40)
	plt.ylabel("Atendimento (%)", fontsize=50)
	plt.yticks(fontsize=40)

	plt.savefig("atendimento3.png")


def graf_utilizacao():
	dados1_Greedy = [25, 25, 25, 16.67, 16.67]
	dados1_DP = [22.92, 25, 25, 18.75, 16.67]
	dados1_GreedyN = [75, 79.17, 58.33, 54.17, 16.67]
	dados1_GTA = [62.5, 81.25, 66.67, 56.25, 16.67]

	erro1_margem_Greedy = [25 * 0.05, 25 * 0.05, 25 * 0.05, 16.67 * 0.05, 16.67 * 0.05]
	erro1_margem_DP = [22.92 * 0.05, 25 * 0.05, 25 * 0.05, 18.75 * 0.05, 16.67 * 0.05]
	erro1_margem_GreedyN = [75 * 0.05, 79.17 * 0.05, 58.33 * 0.05, 54.17 * 0.05, 16.67 * 0.05]
	erro1_margem_GTA = [62.5 * 0.05, 81.25 * 0.05, 66.67 * 0.05, 56.25 * 0.05, 16.67 * 0.05]

	dados2_Greedy = [25, 16.67, 25, 12.5, 8.33]
	dados2_DP = [22.92, 25, 25, 25, 8.33]
	dados2_GreedyN = [75, 91.67, 75, 56.25, 18.75]
	dados2_GTA = [62.5, 100, 79.17, 57.29, 23.96]

	erro2_margem_Greedy = [25 * 0.05, 16.67 * 0.05, 25 * 0.05, 12.5 * 0.05, 8.33 * 0.05]
	erro2_margem_DP = [22.92 * 0.05, 25 * 0.05, 25 * 0.05, 25 * 0.05, 8.33 * 0.05]
	erro2_margem_GreedyN = [75 * 0.05, 91.67 * 0.05, 75 * 0.05, 56.25 * 0.05, 18.75 * 0.05]
	erro2_margem_GTA = [62.5 * 0.05, 100 * 0.05, 79.17 * 0.05, 57.29 * 0.05, 23.96 * 0.05]

	dados3_Greedy = [25, 22.22, 19.44, 25, 19.44]
	dados3_DP = [22.92, 25, 25, 25, 20.83]
	dados3_GreedyN = [75, 86.11, 73.61, 72.22, 31.94]
	dados3_GTA = [62.5, 100, 93.75, 73.61, 34.03]

	erro3_margem_Greedy = [25 * 0.05, 22.22 * 0.05, 19.44 * 0.05, 25 * 0.05, 19.44 * 0.05]
	erro3_margem_DP = [22.92 * 0.05, 25 * 0.05, 25 * 0.05, 25 * 0.05, 20.83 * 0.05]
	erro3_margem_GreedyN = [75 * 0.05, 86.11 * 0.05, 73.61 * 0.05, 72.22 * 0.05, 31.94 * 0.05]
	erro3_margem_GTA = [62.5 * 0.05, 100 * 0.05, 93.75 * 0.05, 73.61 * 0.05, 34.03 * 0.05]

	barWidth = 0.20
	plt.figure(figsize=(31,25))

	r1 = np.arange(len(dados1_Greedy))
	r2 = [x + barWidth for x in r1]
	r3 = [x + barWidth for x in r2]
	r4 = [x + barWidth for x in r3]


	plt.bar(r1, dados1_Greedy, color="aquamarine", width=barWidth, label="Greedy", yerr=erro1_margem_Greedy)
	plt.bar(r2, dados1_DP, color="turquoise", width=barWidth, label="DP",yerr=erro1_margem_DP)
	plt.bar(r3, dados1_GreedyN, color="slateblue", width=barWidth, label="Greedy-N",yerr=erro1_margem_GreedyN)
	plt.bar(r4, dados1_GTA, color="blueviolet", width=barWidth, label="GTA",yerr=erro1_margem_GTA)


	plt.title("Recursos por veículo ω = 1", fontsize=50)
	plt.legend(loc='best', fontsize=40)
	plt.xlabel("Peso médio Tarefa (λ)", fontsize=50)
	plt.xticks([r + barWidth for r in range(len(dados1_Greedy))],["1","5","10","15","20"], fontsize=40)
	plt.ylabel("Utilização (%)", fontsize=50)
	plt.yticks(fontsize=40)

	plt.savefig("utilizacao1.png")

	plt.figure(figsize=(31,25))

	r1 = np.arange(len(dados2_Greedy))
	r2 = [x + barWidth for x in r1]
	r3 = [x + barWidth for x in r2]
	r4 = [x + barWidth for x in r3]


	plt.bar(r1, dados2_Greedy, color="aquamarine", width=barWidth, label="Greedy", yerr=erro2_margem_Greedy)
	plt.bar(r2, dados2_DP, color="turquoise", width=barWidth, label="DP",yerr=erro2_margem_DP)
	plt.bar(r3, dados2_GreedyN, color="slateblue", width=barWidth, label="Greedy-N",yerr=erro2_margem_GreedyN)
	plt.bar(r4, dados2_GTA, color="blueviolet", width=barWidth, label="GTA",yerr=erro2_margem_GTA)


	plt.title("Recursos por veículo ω = 2", fontsize=50)
	plt.legend(loc='best', fontsize=40)
	plt.xlabel("Peso médio Tarefa (λ)", fontsize=50)
	plt.xticks([r + barWidth for r in range(len(dados2_Greedy))],["1","5","10","15","20"], fontsize=40)
	plt.ylabel("Utilização (%)", fontsize=50)
	plt.yticks(fontsize=40)

	plt.savefig("utilizacao2.png")

	plt.figure(figsize=(31,25))

	r1 = np.arange(len(dados3_Greedy))
	r2 = [x + barWidth for x in r1]
	r3 = [x + barWidth for x in r2]
	r4 = [x + barWidth for x in r3]


	plt.bar(r1, dados3_Greedy, color="aquamarine", width=barWidth, label="Greedy", yerr=erro3_margem_Greedy)
	plt.bar(r2, dados3_DP, color="turquoise", width=barWidth, label="DP",yerr=erro3_margem_DP)
	plt.bar(r3, dados3_GreedyN, color="slateblue", width=barWidth, label="Greedy-N",yerr=erro3_margem_GreedyN)
	plt.bar(r4, dados3_GTA, color="blueviolet", width=barWidth, label="GTA",yerr=erro3_margem_GTA)


	plt.title("Recursos por veículo ω = 3", fontsize=50)
	plt.legend(loc='best', fontsize=40)
	plt.xlabel("Peso médio Tarefa (λ)", fontsize=50)
	plt.xticks([r + barWidth for r in range(len(dados3_Greedy))],["1","5","10","15","20"], fontsize=40)
	plt.ylabel("Utilização (%)", fontsize=50)
	plt.yticks(fontsize=40)

	plt.savefig("utilizacao3.png")

def graf_cpu():
	dados_Greedy = [1.87, 1.99, 2.33]
	dados_GreedyN = [5.52, 6.29, 7.09]
	dados_DP = [4.29, 4.20, 4.23]
	dados_GTA = [0.69, 0.68, 0.66]	

	erro_margem_Greedy = [1.87 * 0.05, 1.99 * 0.05, 2.33 * 0.05]
	erro_margem_GreedyN = [5.52 * 0.05, 6.29 * 0.05, 7.09 * 0.05]
	erro_margem_DP = [4.29 * 0.05, 4.20 * 0.05, 4.23 * 0.05]
	erro_margem_GTA = [0.69 * 0.05, 0.68 * 0.05, 0.66 * 0.05]

	barWidth = 0.20

	plt.figure(figsize=(310,25))

	r1 = np.arange(len(dados_Greedy))
	r2 = [x + barWidth for x in r1]
	r3 = [x + barWidth for x in r2]
	r4 = [x + barWidth for x in r3]


	plt.bar(r1, dados_Greedy, color="aquamarine", width=barWidth, label="Greedy", yerr=erro_margem_Greedy)
	plt.bar(r2, dados_GreedyN, color="turquoise", width=barWidth, label="Greedy-N",yerr=erro_margem_GreedyN)
	plt.bar(r3, dados_DP, color="slateblue", width=barWidth, label="DP",yerr=erro_margem_DP)
	plt.bar(r4, dados_GTA, color="blueviolet", width=barWidth, label="GTA",yerr=erro_margem_GTA)


	plt.legend(loc='best', fontsize=14)
	plt.xlabel("Recursos (#)", fontsize=18)
	plt.xticks([r + barWidth for r in range(len(dados_Greedy))],["1","2","3","4"])
	plt.ylabel("Tempo de CPU (s)", fontsize=18)

	plt.show()

graf_recompensa()
graf_atendimento()
graf_utilizacao()
graf_cpu()