# vcloud-python3

Combinatorial Optimization-based Task Allocation Mechanism for Vehicular Clouds

### EXECUTAR:

> ./run.sh CENARIO INTERVALO_DE_CLUSTERIZACAO RECURSOS PESO_MEDIO_TAREFA

### EXECUTAR com Gnu Parallel:

> parallel -j n ./run.sh CENARIO INTERVALO_DE_CLUSTERIZACAO FINAL RAIO ::: {1,...,j} ::: {1,..,k}

onde:

* n: número de núcleos
* {1,...,j}: vetor de recursos disponíveis para alocação
* {1,...,k}: vetor de peso médio das tarefas
* Ver documentação do gnu parallel para mais parâmetros do mesmo

### Comparativos:

* Algoritmo Guloso (knapsack problema OU busca pelo cluster que tenha os recursos (C(X)) >= X)
* Algoritmo de Programação Dinâmica (knapsack problema 0-1)
* Algoritmo baseado em distância (cluster mais proximo?)

### Requisitos:

- Python >= 3.5
- SUMO >= 0.29.0
- sudo apt install python-tk
- sudo apt install parallel
- pip install --user setuptools
- pip install --user virtualenv

### Uso com VirtualEnv Python 3:

- virtualenv venv
- source venv/bin/activate
- pip install --user -r requirements.txt
- deactivate (para sair do ambiente)
