# importamos las librerías que vamos a usar
from flask import  Flask, request, jsonify
import pandas as pd
import numpy as np
import json

CPU_MAX_TEMP=35 #### TEMPERATURA EN `C ,EN LA CUAL EL SERVIDOR CLOUD ENVIA UNA RESPUESTA SI LA TEMPERATURA ENVIADA ES MAYOR

app = Flask('Mirgor_CLOUD_SERVER')

@app.route("/api_cloud",methods=['POST'])
def POST_CLOUD():
    data = request.get_json(force=True)
    #### VERIFICAMOS QUE ESTEN LOS DATOS DE LAS QUERIES , DE EXISTIR HACEMOS UNA ACCION CON ESTOS:
    if 'p1' in data:
        if (data['p1']>35):
            data['p1']="CPU_TEMP_HIGH"#### LA TEMEPERATURA DEL CPU ES ALTA
        else:
            data['p1']="CPU_TEMP_OK" #### LA TEMPERATURA DEL CPU ESTA EN RANGOS ACEPTABLES
    if 'p2' in data:#### HAGO DISTINTAS OPERACIONES CON LOS PROCESOS RECIBIDOS
        data['p2']-=2
    if 'p3' in data:
        data['p3']=data['p3']*2
    if 'p4' in data:
        data['p4']=data['p4']*3
    if 'p5' in data:
        data['p5']=data['p5']+5
    
    
    return data
    
app.run(host='0.0.0.0', port = 5003)
