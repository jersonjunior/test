import requests
import json
r = requests.post('http://127.0.0.1:5005/webhooks/rest/webhook', verify=False,
#data=json.dumps({"sender":"5561998002190","message":"escolho informações"}),
#data=json.dumps({"sender":"5561998002192", "message":"/beneficio_seguro_bf_suspenso"}),
data=json.dumps({"sender":"5561998002192", "message":"A restrição específica foi encerrada."}),
headers={'Accept': 'application/json', 'Content-Type': 'application/json'})
#r.encoding = 'utf-8z-sig'
resposta = json.loads(r.text)
