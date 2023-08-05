import requests #importamo la libreria

response = requests.get("https://api.github.com")
print("")
print(response)# no se ve los headers
print("")
print(response.headers) # se ven los headers
print("")
print(response.status_code)# para conocer el estaod de la respuesta 
print("")
print(response.content)#datos de la respuesta cuerpo o carga pailou - al principio de la repsuesta aparace una b
print("")
print(response.text)#en forma de estring
print("")
print(response.json())#Lo conbierte a uan diccionario de python
print(response.json()["current_user_url"])#de esta forma imprimimos el valor y no toda la respuesta completa

print("")
response = requests.get(
    "https://api.github.com/search/repositories",
    params={"q": "python"}#q query 
)
print(response.status_code)
print("")
print(response.json())

data = response.json()
print(data.keys())# responde dict_keys(['total_count','incomplete_results','items'])
#'total_count' cuantos repositorios encontro
#items cosidensias que tubieran las palabara python
