import pprint

import requests

pp = pprint.PrettyPrinter(indent=4)

consulta = requests.get("https://jsonplaceholder.typicode.com/users")

print(consulta.status_code)
datos = consulta.json()

pp.pprint(datos[0]["address"])