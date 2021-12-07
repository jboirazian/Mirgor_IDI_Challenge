from random import seed
from random import randint
import time
from time import sleep
import requests
import multiprocessing
import json
url = 'http://localhost:5003/api_cloud'
core_temp=27

N_PROCESOS=10 #### Cantidad de procesos

def Proceso_CPU_Temp(ID):
	while True:
		global core_temp
		print(f'Iniciando proceso de actualizacion de temperatura del CPU')
		time.sleep(1)
		core_temp+=1 #### TEST PARA VER COMO CAMBIA LA TEMPERATURA
		print(f'Temperatura actualizada , CPU TEMP ACTUAL: {core_temp}')
		##### PREPARO LOS DATOS Y LOS ENVÍO
		nombre_proceso="p"+str(ID)
		valor_proceso=core_temp
		r = requests.post(url,json={nombre_proceso:(valor_proceso)})
		print(f'Respuesta del servidor Cloud :{r.json()}')
		#####

    
def Proceso_generico(ID,tiempo): 
	###PROCESO GENERICO QUE REALIZA UN SLEEP DEPENDIENDO DE LA VARIABLE "tiempo".
	###una vez que termina envía una request tipo POST al servidor cloud con el formato {pn:tiempo}
	while True:
		print(f'Iniciando proceso que demora {tiempo} segundos')
		time.sleep(tiempo)
		print(f'Proceso que demoró {tiempo} segundos terminado')
		##### PREPARO LOS DATOS Y LOS ENVÍO
		nombre_proceso="p"+str(ID)
		valor_proceso=tiempo
		#####
		print(f'Respuesta enviada al servidor Cloud :{nombre_proceso} : {valor_proceso}')
		r = requests.post(url,json={nombre_proceso:(valor_proceso)})
		print(f'Respuesta del servidor Cloud :{r.json()}')
    
    
seed(123) ### dejo la seed fija para que sea mas facil ver un patrón
tiempos=[]
for i in range(N_PROCESOS):
    tiempos.append(randint(1,3))

def main():
	procesos=[]
	proceso_temp=  multiprocessing.Process(target=Proceso_CPU_Temp,args=[1])
	proceso_temp.start()
	for z in range(2,N_PROCESOS): #### INICIO LOS PROCESOS GENERICOS 
		pro=  multiprocessing.Process(target=Proceso_generico,args=(z+1,tiempos[z]),)
		pro.start()
		print(f"PROCESO {z} INICIADO")
		procesos.append(pro)
		z+=1
	for proceso in procesos:
		proceso.join()



if __name__ == "__main__":
    main()
