# Vistas según patrón MVT (Model View Template)
from flask import render_template

from main import app
from componentes.modelos import Nivel

@app.route('/')
def inicio():
    niveles = Nivel.obtener()
    return render_template('./base.html', datos=niveles)