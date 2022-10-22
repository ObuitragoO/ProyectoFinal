from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

from Controladores.ControladorPartido import ControladorPartido
from __main__ import app

controladorPartido = ControladorPartido()

# Registro de endpoints para las funcionalidades de Mesa
@app.route("/partido", methods=['POST'])
def crearPartido():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controladorPartido.crearPartido(requestBody)
    if result:
        return {"Resultado": "Partido Creado!"}
    else:
        return {"Resultado": "Error al crear el Partido!"}

@app.route("/partido/<string:idObject>", methods=['GET'])
def buscarPartido(idObject):
    result = controladorPartido.buscarPartido(idObject)
    if result is None:
        return {"Resultado": "No se encuentra el partido en base de datos!"}
    else:
        return jsonify(result)

@app.route("/partido", methods=['GET'])
def buscarTodosLosPartidos():
    result = controladorPartido.buscarTodosLosPartidos()
    if not result:
        return {"Resultado": "No se encuentran partidos en la base de datos!"}
    else:
        return jsonify(result)

@app.route("/pardio", methods=['PUT'])
def actualizarPartido():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controladorPartido.actualizarPartido(requestBody)
    if result:
        return {"Resultado": "Partido actualizado!"}
    else:
        return {"Resultado": "Error al actualizar el partido!"}

@app.route("/partido/<string:idObject>", methods=['DELETE'])
def eliminarPartido(idObject):
    result = controladorPartido.eliminarPartido(idObject)
    if result:
        return {"Resultado": "Partido eliminado!"}
    else:
        return {"Resultado": "Error al eliminar el partido!"}


