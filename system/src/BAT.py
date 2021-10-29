# -*- coding: utf-8 -*-
"""
Created on Thu May 26 02:00:55 2016

@author: hossam
"""
import math
import numpy
import random
import time
#from solution import solution

def euclidiana(y,z):
    return (numpy.sqrt(sum((y - z) ** 2))) 


def F10(x):
    dim = len(x)
    o = (
        -20 * numpy.exp(-0.2 * numpy.sqrt(numpy.sum(x ** 2) / dim))
        - numpy.exp(numpy.sum(numpy.cos(2 * math.pi * x)) / dim)
        + 20
        + numpy.exp(1)
    )
    return o

#def BAT(objf, lb, ub, dim, N, Max_iteration):
def bat_solution(sw, Serv_List, MaxIter):
    Fog_nro = sw
    #MaxIter = 8
    #objf é o banchmark utilizado
    dim = 2
    #n = 30
    n = dim

    Nro_serv = len(Serv_List)
    #N - Population size
    #print("sw = ", sw)
    #print("Serv_List = ", Serv_List)
    #print("MaxIter = ", MaxIter)
    #print("Nro_serv = ", Nro_serv)


    #lb - lower boundary - Limite
    #ub - upper boundary - Limite

    #if not isinstance(lb, list):
    #    lb = [lb] * dim
    #if not isinstance(ub, list):
    #    ub = [ub] * dim

    #N_gen = MaxIter  # Number of generations

    A = 0.5
    # Loudness  (constant or decreasing)
    r = 0.5
    # Pulse rate (constant or decreasing)

    Qmin = 0  # Frequency minimum
    Qmax = 2  # Frequency maximum

    d = dim  # Number of dimensions

    # Initializing arrays
    Q = numpy.zeros(Nro_serv)  # Frequency
    v = numpy.zeros((Nro_serv, dim))  # Velocities
    Convergence_curve = []

    # Initialize the population/solutions
    Sol = numpy.zeros((Nro_serv, dim))
    for i in range (0, dim):
        for j in range(0, Nro_serv):
            y = numpy.array([Serv_List[j][i+1]])
            z = numpy.array(sw)
            Sol[j, i] = euclidiana(y,z)
    S = numpy.zeros((Nro_serv, dim))
    #print("S = ", S)
    S = numpy.copy(Sol)
    #print("S = ", S)
    Fitness = numpy.zeros(Nro_serv)

    # initialize solution for the final results
    #s = solution()
    #print('BAT is optimizing  "' F10.__name__'"')

    # Initialize timer for the experiment
    timerStart = time.time()
    #s.startTime = time.strftime("%Y-%m-%d-%H-%M-%S")

    # Evaluate initial random solutions
    for i in range(0, Nro_serv):
        Fitness[i] = F10(Sol[i, :])

    # Find the initial best solution and minimum fitness
    I = numpy.argmin(Fitness)
    best = Sol[I, :]
    fmin = min(Fitness)
    Best = I
    #print ("MAIN LOOP")
    #print("Fitness = ", Fitness)
    #print("MaxIter = ", MaxIter)
    #print("Nro_serv = ", Nro_serv)
    #print("Best = ", Best)

    # Main loop
    for t in range(0, MaxIter): #loop de 0 até numero de iterações
        # Loop over all bats(solutions)
        for i in range(0, Nro_serv): #loop de 0 até número de população
            Q[i] = Qmin + (Qmin - Qmax) * random.random()
            v[i, :] = v[i, :] + (Sol[i, :] - best) * Q[i]
            S[i, :] = Sol[i, :] + v[i, :]
            # Check boundaries
            #for j in range(d):
            #    Sol[i, j] = numpy.clip(Sol[i, j], lb[j], ub[j])

            # Pulse rate
            if random.random() > r:
                S[i, :] = best + 0.001 * numpy.random.randn(d)

            # Evaluate new solutions
            Fnew = F10(S[i, :])
            #print("Fnew = ", Fnew)
            # Update if the solution improves
            #print("------------------------------------------------")
            #print("Fnew <= Fitness[i]")
            #print("Fitness[i] = ", Fitness[i])
            if (Fnew <= Fitness[i]) and (random.random() < A):
                Sol[i, :] = numpy.copy(S[i, :])
                Fitness[i] = Fnew
                Best = i              
                #print("Best = ", Best)

            #print("------------------------------------------------")
            #print("Fnew <= fmin")
            #print("Fnew = ", Fnew)
            #print("fmin = ", fmin)
            # Update the current best solution
            if Fnew <= fmin:
                best = numpy.copy(S[i, :])
                fmin = Fnew
                Best = i         
                #print("Best = ", Best)     

        # update convergence curve
        #Convergence_curve.append(fmin)

        #if t % 1 == 0:
        #    print(["At iteration " + str(t) + " the best fitness is " + str(fmin)])

 #   timerEnd = time.time()
 #  s.endTime = time.strftime("%Y-%m-%d-%H-%M-%S")
 #   s.executionTime = timerEnd - timerStart
 #  s.convergence = Convergence_curve
 #   s.optimizer = "BAT"
 #   s.objfname = F10.__name__

 #   return s
    #print("Best antes do return: ", Best)
    return Best





def bat(W, T):
    MaxIter = len(T)
    vi = 0
    #sw = 0 #global sw
    bloqueio = 0
    g = 0 #tempo = 0.0
    gain_mors = 0
    alocadas = 0
    nao_alocadas = 0
    cont_peso = 0    
    resto = []
    for p in range (0,len(T)):
        T[p][0] = g
        g += 1
    
    VCC=[]
    for j,k in W.items():
        VCC.append(k)

    t1=[]
    g=0
    VCC = sorted(VCC, reverse=True)    
    aloc=[]
    for x in range(0,len(VCC)):
        vi = VCC[x]
        for r in range (0,len(T)):
            T[r][0] = g
            g += 1
        for n in range(0,len(T)):
            t1.append(T[n])
        while (len(t1) > 0):
            if (vi > 0):
                g=0
                for q in range (0,len(t1)):
                    t1[q][0] = g
                    g += 1
                p = bat_solution(vi,t1, MaxIter)
                if ((vi - t1[p][1]) >= 0):
                    t = t1[p]
                    gain_mors += t[2]
                    cont_peso += t[1]
                    alocadas += 1
                    vi -= t[1]
                    aloc = aloc + [t]
                    
                else:
                    bloqueio += 1
                del t1[p]
            else:
                for x in t1:
                    del t1[0]
            
        for x in range(0,len(aloc)):
            for y in range (0,len(T)):
                if (aloc[0][1]==T[y][1] and aloc[0][2]==T[y][2]):
                    del T[y]
                    del aloc[0]
                    break
    return (gain_mors, alocadas, cont_peso)