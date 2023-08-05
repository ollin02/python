import requests

url = "https://webhook.site/74490df8-f2e7-4552-af07-c4cefa0febad"
payload = {"plato": "pasta", "cantidad": 2}#cuerpo de la peticion
#query_params = {"nombre": "Paco"}
response = requests.post(url, data=payload)
query_params = {"nombre": "Paco"}
response = requests.post(url, data=payload, params=query_params)#creamos la petición
print(response.status_code)