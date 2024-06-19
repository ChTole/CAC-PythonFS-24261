from flask import Flask
from flask import jsonify

from componentes.datos import obtener_datos

app = Flask(__name__)

# Vistas
@app.route('/')
def inicio():
    return "<h1>Bienvenid@s a Flask!!!</h1>"

@app.route('/api/test') # http://127.0.0.1:5000/api/test
def mostrar_datos():
    # return obtener_datos() # 'idTest', pero necesito "idTest"
    return jsonify(obtener_datos()) # 'idTest', pero necesito "idTest"

if __name__ == "main":
    app.run()