from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

from Controladores.ControladorResultado import ControladorResultado
from __main__ import app

controladorResultado = ControladorResultado()


# Registro de endpoints para las funcionalidades de Resultado

@app.route("/resultado", methods=['POST'])
def crearResultado():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controladorResultado.crearResultado(requestBody)
    if result:
        return {"resultado": "resultado Creado!"}
    else:
        return {"resultado": "Error al crear el resultado!"}

@app.route("/resultado/<string:idObject>", methods=['GET'])
def buscarResultado(idObject):
    result = controladorResultado.buscarResultado(idObject)
    if result is None:
        return {"resultado": "No se encuentra el resultado en base de datos!"}
    else:
        return jsonify(result)

@app.route("/resultado", methods=['GET'])
def buscarTodosLosResultados():
    result = controladorResultado.buscarTodosLosResultados()
    if not result:
        return {"resultado": "No se encuentran resultado en la base de datos!"}
    else:
        return jsonify(result)

@app.route("/resultado", methods=['PUT'])
def actualizarResultado():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controladorResultado.actualizarResultado(requestBody)
    if result:
        return {"resultado": "resultado actualizado!"}
    else:
        return {"resultado": "Error al actualizar el resultado!"}

@app.route("/resultado/<string:idObject>", methods=['DELETE'])
def eliminarResultado(idObject):
    result = controladorResultado.eliminarResultado(idObject)
    if result:
        return {"resultado": "resultado eliminado!"}
    else:
        return {"resultado": "Error al eliminar el resultado!"}
