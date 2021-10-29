#!/bin/bash

# author: Joahannes Costa <joahannes@lrc.ic.unicamp.br>

TEST=$1

# basico:
#  * cenario: lust
#  * intervalo (s): 60
#  * inicio (s): 100
#  * termino (s): 200
#  * raio (m): 100
#  * recurso (u): 1
#  * peso (u): 50
# completo:
#  * simulacao completa

if [ $TEST == 'basico' ]
then
	./run.sh lust 60 100 200 100 1 50
elif [ $TEST == 'completo' ]
then
	#parallel -j 6 ./run.sh lust 60 50000 58000 100 ::: {1,2,3} ::: {1,25,50,100,200,300}
	
	parallel -j 8 ./run.sh lust 60 100 90000 100 ::: {1,2,3} ::: {1,5,10,15,20} 
else
	echo ">> ERROR: TESTE NAO RECONHECIDO!"
fi
