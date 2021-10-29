def plot_cpu_time():

	print ("\nCPU_TIME:")

	for algorithm in ALGORITHM:

		print (LABEL[algorithm])

		gain_values = []
		gain_values_pli = []
		confidence_intervals = []
		confidence_intervals_pli = []

		for recursos in RECURSO:
			
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

		x = np.arange(len(RECURSO))		
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
	ax.set_xticklabels(RECURSO, fontsize=legenda_size)

	ax.set_axisbelow(True)

	# ax.set_ylim(0, 5000)

	ax.set_yscale('log')

	# plt.title(r'$\mu$ = '+str(tamanho), fontsize=legenda_size)

	plt.grid(color='0.85', linestyle='--', linewidth=0.5, axis='both', alpha=0.1)
	
	fig = plt.gcf()
	fig.set_size_inches(x_tam, y_tam)
	fig.savefig('1706_cputime_barra_'+str(tamanho)+formato, dpi=200, bbox_inches = 'tight', pad_inches = 0.04 )

	plt.close()
