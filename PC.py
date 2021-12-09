from random import seed
from random import randint
import time
from time import sleep
import requests
import multiprocessing
from multiprocessing.connection import Listener,Client
import json
import sys
from pyspectator.processor import Cpu
url = 'http://localhost:5003/api_cloud'
cpu = Cpu(monitoring_latency=1)
N_PROCESOS=5 #### Cantidad de procesos


address = 'localhost' #127.0.0.1
port = 2823 #
contrasenia=b'challenge'

seed(123) ### dejo la seed fija para que sea mas facil ver un patrón
tiempos=[]
for i in range(N_PROCESOS):
    tiempos.append(randint(1,3))


def Proceso_CPU_Temp(ID):
	while True:
		global core_temp
		time.sleep(1)
		##### PREPARO LOS DATOS Y LOS ENVÍO
		nombre_proceso="p"+str(ID)
		valor_proceso=cpu.temperature
		#####
		datos={nombre_proceso:valor_proceso}
		address = 'localhost' #127.0.0.1
		port = 2822#
		dest = (address,port)
		conn = Client(dest,authkey=contrasenia)
		conn.send(datos)

    
def Proceso_generico(ID,tiempo): 
	###PROCESO GENERICO QUE REALIZA UN SLEEP DEPENDIENDO DE LA VARIABLE "tiempo".
	###una vez que termina envía una request tipo POST al servidor cloud con el formato {pn:tiempo}
	while True:
		time.sleep(tiempo)
		##### PREPARO LOS DATOS Y LOS ENVÍO
		nombre_proceso="p"+str(ID)
		valor_proceso=tiempo
		#####
		datos={nombre_proceso:valor_proceso}
		address = 'localhost' #127.0.0.1
		port = 2823 + (ID-1)#
		dest = (address,port)
		conn = Client(dest,authkey=contrasenia)
		conn.send(datos)
		

def Proceso_Enviar_Cloud(server,port,key):
	### INICIAMOS EL PROCESO DE VER SI NOS LLEGAN DATOS A LA DIRECCION
	direccion= (server,port)
	listener=Listener(direccion,authkey=key)
	while True:
		conexion =listener.accept()
		msg = conexion.recv()
		r = requests.post(url,json=msg)
		if int(r.status_code) >= 500: ### si tengo un error de estado del tipo 500 es porque hay un problema con el servidor
			sys.exit(0) ### cierro todo o hago otra cosa en el caso de que haya un error de comunicación
		print(f'#################\n Se envió al servidor {msg} \n\n La Respuesta fué:{r.json()} \n#################\n')
	
    

def main():
	procesos=[]
	procesos_sockets=[]
	proceso_temp=  multiprocessing.Process(target=Proceso_CPU_Temp,args=[1])
	proceso_temp.start()
	
	proceso_envio_datos= multiprocessing.Process(target=Proceso_Enviar_Cloud,args=[address,port-1,contrasenia])
	proceso_envio_datos.start()
	
	for z in range(2,N_PROCESOS): #### INICIO LOS PROCESOS DE COMUNICACÍON
		puerto=port + z
		proceso_envio_datos=  multiprocessing.Process(target=Proceso_Enviar_Cloud,args=[address,puerto,contrasenia])
		proceso_envio_datos.start()
		print(f"INICIANDO PROCESO DE COMUNICACIÓN LOCAL EN EL PUERTO {puerto}")
		procesos_sockets.append(proceso_envio_datos)
		z+=1
		
	
	for y in range(2,N_PROCESOS): #### INICIO LOS PROCESOS GENERICOS 
		pro=  multiprocessing.Process(target=Proceso_generico,args=(y+1,tiempos[y]),)
		pro.start()
		print(f"PROCESO {y} INICIADO")
		procesos.append(pro)
		y+=1



if __name__ == "__main__":
    main()
