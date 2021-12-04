# importamos las librerías que vamos a usar
from flask import  Flask, request, jsonify
import pandas as pd
import numpy as np
import json

app = Flask('Mirgor_CLOUD_SERVER')

# Definimos un nuevo endoint o resource path (prueba_get) y explicitamos el método.
@app.route("/api_cloud",methods=['POST'])
def pruebaGet():
    data = request.get_json(force=True)
    data['p1']+=2
    data['p2']-=2
    data['p3']=data['p3']*2
    data['pN']=data['pN']/2
    
    return data
    
app.run(host='0.0.0.0', port = 5003)
