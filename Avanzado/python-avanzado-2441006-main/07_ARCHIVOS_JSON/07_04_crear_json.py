import json

persona = {
    "nombre": "Javier",
    "apellido": "Quinonez",
    "edad": 24
}
# objeto_json = json.dumps(persona, indent=2)/ se hace la serialización

with open("persona.json", "w") as archivo_json:
    # archivo_json.write(objeto_json)/ describimos nuestr archivo
    json.dump(persona, archivo_json)
