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
        return {"Resultado": "Mesa Creada!"}
    else:
        return {"Resultado": "Error al crear la Mesa!"}

@app.route("/mesa/<string:idObject>", methods=['GET'])
def buscarMesa(idObject):
    result = controladorMesa.buscarMesa(idObject)
    if result is None:
        return {"Resultado": "No se encuentra la mesa en base de datos!"}
    else:
        return jsonify(result)

@app.route("/mesa", methods=['GET'])
def buscarTodasLasMesas():
    result = controladorMesa.buscarTodasLasMesas()
    if not result:
        return {"Resultado": "No se encuentran mesas en la base de datos!"}
    else:
        return jsonify(result)

@app.route("/mesa", methods=['PUT'])
def actualizarMesa():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controladorMesa.actualizarMesas(requestBody)
    if result:
        return {"Resultado": "Mesa actualizada!"}
    else:
        return {"Resultado": "Error al actualizar el Mesa!"}

@app.route("/mesa/<string:idObject>", methods=['DELETE'])
def eliminarEstudiante(idObject):
    result = controladorMesa.eliminarMesa(idObject)
    if result:
        return {"Resultado": "Mesa eliminada!"}
    else:
        return {"Resultado": "Error al eliminar la Mesa!"}


