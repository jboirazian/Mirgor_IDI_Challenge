# Mirgor_IDI_Challenge
Desafío técnico 2021


Desarollado en 2 .py , **Cloud_server.py** y **PC.py**





## Como correrlo:

Primero instalar los modulos con pip:
```python
pip install -r requierements.txt
```

Luego iniciar el servidor:

```python
python Cloud_server.py
```
Nota:el servidor es hosteado de manera local en host='0.0.0.0', port = 5003

Despues correr el cliente en simultaneo en una terminal diferente:
```python
python PC.py
```

### Diagrama esquemático:

![comunicacíon](https://user-images.githubusercontent.com/21143405/144876666-8fa1cf70-22ff-4f36-91fb-60b0eee099b0.jpg) 


### Preguntas de interés en la devolucion:

* En caso de que el sistema no tenga conectividad hacia el exterior, ¿Qué estrategia utilizaría para evitar pérdida de datos críticos? Proponga herramientas y/o estrategias que se podrían utilizar para dicho fin.

#### -> Respuesta:

A la hora de enviar los datos al servidor cloud verficar de manera provisoria la conexion. Si hacemos una request al servidor y este devuelve un codigo de estado del tipo 50X (500,502,503,504) significa que existe algun error del lado de la conectividad con el Cloud.
De ocurrir esto se podría :

1) Guardar los datos en un archivo y enviarlos cuando la conexion se restablezca (haciendo pings al servidor luego de una determinada cantidad de tiempo para ver si el codigo de estado de la request cambia)
2) Enviar los datos a un servidor local y que este se encargue de enviarlos cuando la conexion se restablezca.



* ¿Qué problemas encuentra en la arquitectura propuesta para el sistema? Proponga soluciones a los mismos y consecuencias de dichos cambios.


#### -> Respuesta: 
En la arquitectura propuesta en ningun momentó se tiene en cuenta la prioridad de los procesos.Esto puede llegar a ser un problema en el caso de que uno o mas procesos importantes para nuestro proyecto debena informar de algun suceso importante.

* ¿Qué cambios considera serían necesarios para adaptar la solución propuesta funcionando en una PC para que funcione en una computadora embebida (RaspberryPi, BeagleBone, etc...)


#### -> Respuesta:
Encuentro que requiere de muchos recursos.Considero que será necesario evaluar los recursos disponibles en la computadora embebida , ya que al disponer de un procesador ARM ( single , dual o quad core dependiendo de los casos). La adaptabilidad de solucíon propuesta dependerá de la cantidad de procesos que tenga nuestro proyecto.

De tener una cantidad considerable podriamos:

* Disminuir la carga en nuestro CPU agrupando multiples procesos en uno solo. Haciendo que sus tareas ocurran de manera secuencial y no de manera paralela ( para esto debemos evaluar la importancia de cada uno de los procesos de manera indiviual). De esta manera ahorraremos recursos en el CPU , pero perderemos velocidad en la resolucíon de procesos.

* Reemplazar la metodología de comunicacíon de Sockets/TCP entre procesos por una comunicacíon utilizando archivos , donde por ejemplo: un proceso *A* escribe un archivo y luego uno o varios procesos leén dicho archivo. De esta manera no hace falta esta que cada procesos este ¨escuchando¨ un puerto de manera constante esperando los datos , ahorrando recursos en el procesador.

* Al estar contenido en una computadora embebida , probablemente todos los procesos se originen de un mismo .py , por lo que podría obviar usar Sockets para comunicarme entre procesos y utilizar una cola/queue para comunicarme entre los distintos procesos.




### TO-DO LIST:

- [x] Primera implementacion con cantidad de procesos fija
- [x] POST cpu temperature method
- [x] Agregar Proxy
- [x] Hacer que sea dinamico para multiples procesos
- [x] Diagrama en bloques
- [x] Proponga un diagrama de bloques y un diagrama de secuencia del funcionamiento del proceso.
- [ ] Agregar conexion TCP entre los distintos procesos
- [ ] Hostear en Heroku a Cloud_server.py si tengo tiempo
