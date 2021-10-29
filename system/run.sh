#!/bin/bash
# Autor: Joahannes B.D. da Costa <joahannes@lrc.ic.unicamp.br>
# Data: 13.07.2019
# Rodar: ./run.sh cenario intervalo_de_clusterizacao inicio final raio_comunicacao recursos peso_medio_tarefa info

CENARIO=$1
INTERVALO=$2
BEGIN=$3
END=$4
RAIO=$5
RESOURCE=$6
WEIGHT_TASK=$7

if [ -z $CENARIO ] || [ -z $INTERVALO ]
then
	echo " >> Verifique os parametros: cenario intervalo inicio fim raio recursos peso"

elif [ $CENARIO == 'sp' ]
then
	#===================================#
	#									#
	#			SAO PAULO				#
	#									#
	#===================================#
	echo 'Cenario:' $CENARIO
	echo 'Intervalo:' $INTERVALO's'
	echo 'Inicio em:' $BEGIN's'
	echo 'Final em:' $END's'
	echo 'Radio de:' $RAIO'm'
	echo 'Recurso por veiculo:' $RESOURCE
	echo 'Peso medio de cada tarefa:' $WEIGHT_TASK
	python src/main.py -s scenario/sp/sim-v2.sumo.cfg -n scenario/sp/sim-v2.net.xml -i $INTERVALO -b $BEGIN -e $END -o output/sim-v2-output.xml -l log/sim-v2-log.xml -m summary/sim-v2.summary.xml -t $RAIO -r $RESOURCE -w $WEIGHT_TASK

elif [ $CENARIO == 'lust' ]
then
	#===================================#
	#									#
	#			LUXEMBURGO				#
	#									#
	#===================================#
	echo 'Cenario:' $CENARIO
	echo 'Intervalo:' $INTERVALO's'
	echo 'Inicio em:' $BEGIN's'
	echo 'Final em:' $END's'
	echo 'Radio de:' $RAIO'm'
	echo 'Recurso por veiculo:' $RESOURCE
	echo 'Peso medio de cada tarefa:' $WEIGHT_TASK
	python3 src/main.py -s scenario/lust/dua.static.sumocfg -n scenario/lust/lust.net.xml -i $INTERVALO -b $BEGIN -e $END -o output/lust-output.xml -l log/lust-log.xml -m summary/lust.summary.xml -t $RAIO -r $RESOURCE -w $WEIGHT_TASK
else
	echo ">> Cenario nao reconhecido!"
fi
