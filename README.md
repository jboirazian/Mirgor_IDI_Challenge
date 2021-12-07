# Mirgor_IDI_Challenge
Desafío técnico 2021


Desarollado en 2 .py , Cloud_server.py y PC.py





## Como correrlo:
Primero iniciar el servidor:

```python
python Cloud_server.py
```
Nota:el servidor es hosteado de manera local en host='0.0.0.0', port = 5003

Luego correr el cliente en simultaneo en una terminal diferente:
```python
python PC.py
```

### Diagrama esquemático:

![comunicacíon](https://user-images.githubusercontent.com/21143405/144876666-8fa1cf70-22ff-4f36-91fb-60b0eee099b0.jpg) 


### Preguntas de interés en la devolucion:

* En caso de que el sistema no tenga conectividad hacia el exterior, ¿Qué estrategia utilizaría para evitar pérdida de datos críticos? Proponga herramientas y/o estrategias que se podrían utilizar para dicho fin.

Respuesta: A la hora de enviar los datos al servidor cloud verficar de manera provisoria la conexion. Si hacemos una request al servidor y este devuelve un codigo de estado del tipo 50X (500,502,503,504) significa que existe algun error del lado de la conectividad con el Cloud.
De ocurrir esto se podría :

1) Guardar los datos en un archivo y enviarlos cuando la conexion se restablezca (haciendo pings al servidor luego de una determinada cantidad de tiempo para ver si el codigo de estado de la request cambia)
2) Enviar los datos a un servidor local y que este se encargue de enviarlos cuando la conexion se restablezca.

la opción

* ¿Qué problemas encuentra en la arquitectura propuesta para el sistema? Proponga soluciones a los mismos y consecuencias de dichos cambios.

* ¿Qué cambios considera serían necesarios para adaptar la solución propuesta funcionando en una PC para que funcione en una computadora embebida (RaspberryPi, BeagleBone, etc...)




### TO-DO LIST:

- [x] Primera implementacion con cantidad de procesos fija
- [x] POST cpu temperature method
- [x] Agregar Proxy
- [x] Hacer que sea dinamico para multiples procesos
- [x] Diagrama en bloques
- [x] Proponga un diagrama de bloques y un diagrama de secuencia del funcionamiento del proceso.
- [ ] Agregar conexion TCP entre los distintos procesos
- [ ] Hostear en Heroku a si tengo Cloud_server.py tiempo 
