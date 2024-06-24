# Vistas para la arquitectura API REST
from flask import jsonify

from main import app
from componentes.modelos import Docente
from componentes.modelos import Nivel


@app.route('/api-edtech/docentes')
def mostrar_docentes():
    docentes = Docente.obtener()
    docentes_dicc = [d.__dict__ for d in docentes]
    return jsonify(docentes_dicc)