from random import seed
from random import randint
import time
from pyspectator.processor import Cpu
from time import sleep
import requests

url = 'http://localhost:5003/api_cloud'
cpu = Cpu(monitoring_latency=1)
while True:
    sleep(1)
    seed(time.time())
    datos={'p1' : cpu.temperature,'p2' : randint(0,100),'p3' : randint(0,50) , 'pN':randint(0,120)}
    r = requests.post(url,json=datos)
    
    print(r.json())
