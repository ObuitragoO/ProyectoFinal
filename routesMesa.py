from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

from Controladores.ControladorMesa import ControladorMesa
from __main__ import app

controladorMesa = ControladorMesa()

# Registro de endpoints para las funcionalidades de Mesa
@app.route("/mesa", methods=['POST'])
def crearMesa():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controladorMesa.crearMesa(requestBody)
    if result:
        return {"resultado": "Mesa Creada!"}
    else:
        return {"resultado": "Error al crear la Mesa!"}

@app.route("/mesa/<string:idObject>", methods=['GET'])
def buscarMesa(idObject):
    result = controladorMesa.buscarMesa(idObject)
    if result is None:
        return {"resultado": "No se encuentra la mesa en base de datos!"}
    else:
        return jsonify(result)

@app.route("/mesa", methods=['GET'])
def buscarTodasLasMesas():
    result = controladorMesa.buscarTodasLasMesas()
    if not result:
        return {"resultado": "No se encuentran mesas en la base de datos!"}
    else:
        return jsonify(result)

@app.route("/mesa", methods=['PUT'])
def actualizarMesa():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controladorMesa.actualizarMesas(requestBody)
    if result:
        return {"resultado": "Mesa actualizada!"}
    else:
        return {"resultado": "Error al actualizar el Mesa!"}

@app.route("/mesa/<string:idObject>", methods=['DELETE'])
def eliminarEstudiante(idObject):
    result = controladorMesa.eliminarMesa(idObject)
    if result:
        return {"resultado": "Mesa eliminada!"}
    else:
        return {"resultado": "Error al eliminar la Mesa!"}

