#import benchmarks as bench
import random
import numpy

sw = 0 #soma de resursos

def euclidiana(y,z):
    # x, y, z = C, XP, X
    return (numpy.sqrt(sum((y - z) ** 2))) #distancia euclidiana

def update_Coeficientes(a):
    
    r1 = random.randrange(0,11)/10
    r2 = random.randrange(0,11)/10
    C = 2*r2
    A = 2*a*r1-a
    
    return A,C


def F6(x):
    o=numpy.sum(abs((x+.5))**2);
    return o;

def gwo_solution(W, Serv_List):
    #Fog_nro = sw
    MaxIter = 10
    dim = 2

    Pos = {}
    Nro_serv = len(Serv_List)

    Alpha = numpy.zeros(1)
    Alpha_pos = numpy.zeros(dim)
    Alpha_score = float("inf")

    Beta = numpy.zeros(1)
    Beta_pos = numpy.zeros(dim)
    Beta_score = float("inf")

    Delta = numpy.zeros(1)
    Delta_pos = numpy.zeros(dim)
    Delta_score = float("inf")

    Positions = numpy.zeros((Nro_serv,2))

    for i in range(0,dim):
        for j in range(0, Nro_serv):
            #print ([Serv_List[j][i+1]])
            y = numpy.array([Serv_List[j][i+1]])
            x = numpy.array([Fog_nro])
            p = euclidiana(x,y)
            Positions[j,i] = p
            #Positions[j,i] = y
    #print (Positions)
    aux = (2/MaxIter)
    a = 2
    A, C = update_Coeficientes(a)
    
    for l in range(0,MaxIter): #máximo de iterações

        for j in range(0,Nro_serv): #passar por todos os serviços
                   
            fitness = F6(Positions[j,:])
                
            
            if (fitness < Alpha_score):
                
                Alpha = j
                Alpha_score = fitness
                Alpha_pos=Positions[j,:].copy()
            elif (fitness > Alpha_score and fitness < Beta_score):
                
                Beta = j
                Beta_score = fitness
                Beta_pos=Positions[j,:].copy()
            elif (fitness > Alpha_score and fitness < Beta_score and fitness < Delta_score):
            
                Delta = j
                Delta_score = fitness
                Delta_pos=Positions[j,:].copy()
            
        a = a - aux 
        
        for i in range(0,Nro_serv):
            for j in range (0,dim):
                #X = numpy.array([Fog_nro])
                
                #atualiza_Coeficientes(a)
                #a = a - aux
                A1, C1 = update_Coeficientes(a)
                D_alpha=abs(C1*Alpha_pos[j]-Positions[i,j]); # Equation ()-part 1
                X1=Alpha_pos[j]-A1*D_alpha; # Equation ()
                #a = a - aux    
                A2, C2 = update_Coeficientes(a)
                D_beta=abs(C2*Beta_pos[j]-Positions[i,j]); # Equation ()
                X2=Beta_pos[j]-A2*D_beta; # Equation ()       
                #a = a - aux    
                A3, C3 = update_Coeficientes(a)
                D_delta=abs(C3*Delta_pos[j]-Positions[i,j]); # Equation ()
                X3=Delta_pos[j]-A3*D_delta; # Equation ()             

                Positions[i,j] =(X1+X2+X3)/3  # Equation ()
                
        #print(['At iteration '+ str(l)+ ' the best fitness is '+ str(Alpha_score)]);
    return Alpha        

def gwo(W, T):
    #sw = 0 #global sw
    print ("W gwo: ", W)
    bloqueio = 0
    #atendimento = 0
    #tempo = 0.0
    gain_mors = 0
    alocadas = 0
    nao_alocadas = 0
    cont_peso = 0    
    resto = []
    #W = {0: 20, 1: 30, 2: 40}
    w = []
    for j,k in W.items():
        w.append(k)
    
    w = sorted(w, reverse=True)

    #print (W)
    #print (w)
    #print ("Tarefas: ", T)
    if (len(T) > 0):
        for x in range(0,len(W)):
            #print ("Mudar posição W: ", x)
            for s in range (0,len(T)):
                
                for k in range(0,len(T)-1):
                    T[k][0] = k

                p = gwo_solution(w,T)

                #print("w[x]: ", w[x])
                #print("Valor: ", T[p][1])

                if ((w[x] - T[p][1]) >= 0):
                    
                    t = T.pop(p)
                    gain_mors += t[2]
                    alocadas += 1
                    cont_peso += t[1]
                    w[x] -= t[1]
                    
                    #print ("sw e t1: ", sw, t[1])
                else:
                    bloqueio += 1
                    #resto += [T.pop(p)]
            #else:
            #     print ("Não coube: ")
            #     nao_alocadas=len(T)
                #     #break
                if ((len(T) == 0) or (w[x] == 0)):
                    break
        #print ("chegou final SW: " , sw)
        #print ("Resto:  ", resto)
    return gain_mors, alocadas, cont_peso
    



#for x in range (0,2):
#    ex = [[0,12,14],[1,12,19],[2,3,5],[3,21,19],[4,12,1],[5,2,4],[6,1,4],[7,17,5],[8,16,14],[9,7,5], [10,1,3], [11,3,18], [12,34,14]]
#    te = {0: 20, 1: 30, 2: 60}
#   print ("Aleluia: ", gwo(te,ex))
