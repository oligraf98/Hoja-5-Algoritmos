#Alexa Bravo 18831
#Oliver Graf 17190
#Estructura de Datos
#Hoja5
#Febrero 28, 2019

import simpy
import random
import statistics
 
#random.expovariate(1.0/interval)
 
#Para el ram
#Container con 100 de ram
 
#El CPU atiende un proceso en 1 unidad de tiempo.
#resorce con capacidad = 1 porque solo hay un cpu
 
#Para generar numeros que sea siempre la misma secuencia se usa
#random.seed(RANDOM_SEED)
 
 
#=========================================================
def proceso(env, cpu, ram, ramNecesitado, x):
    instanteDeInicio = env.now
   
    with ram.get(ramNecesitado) as espacioEnMemoria:
        yield espacioEnMemoria
        if x > 2:
 
            while x > 2:
                with cpu.request() as req:
 
                    yield req
                    yield env.timeout(1)    
 
                    x = x - 3
                r = random.randint(1, 2)
                if r == 2:
 
                    yield env.timeout(1)
        else:
            with cpu.request() as req:
               
                    yield req
 
                    yield env.timeout(1)  
 
       
    ram.put(ramNecesitado)
    resultados.append(env.now - instanteDeInicio)
    print('Proceso terminado en:', (env.now))
 
    env.exit()  
   
   
def compu(env, cpu, ram, inProcesos, inRitmo):
 
    for x in range(inProcesos):
        yield env.timeout(random.expovariate(1/inRitmo))
        print('Proceso No.', x + 1)
        print('Tick actual:', env.now)
        print('')
        env.process(proceso(env, cpu = cPu, ram = rAm, ramNecesitado=random.randint(1, 10), x=random.randint(1, 10)))
 
   
 
#=========================================================
#Inicia el programa
env = simpy.Environment()
random.seed(10)
 
#Datos
resultados = []
rAm = simpy.Container(env, capacity = 100, init = 100)
cPu = simpy.Resource(env, capacity=1)
 
 
print('Ingrese el numero de procesos que quiere que se lleven a cabo: ')
in1 = input()
while not in1.isdigit():
    print('Por favor ingrese un numero')
    print('intentelo de nuevo')
    in1 = input()
in1 = int(in1)
 
 
print('Ingrese el ritmo al que se generaran los procesos: ')
in2 = input()
while not in2.isdigit():
    print('Por favor ingrese un numero')
    print('intentelo de nuevo')
    in2 = input()
in2 = int(in2)
env.process(compu(env, rAm, cPu, inProcesos = in1, inRitmo = in2))
env. run()
 
print('')
print('RESULTADOS')
print('')
promedio = statistics.mean(resultados)
print('Promedio: %.4f' % promedio)
desviacionEst = statistics.stdev(resultados)
print(' Desviacion estandard: %.4f' % desviacionEst)
