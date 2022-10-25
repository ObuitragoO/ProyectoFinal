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
    if result == {}:
        result = {}
        result["message"] = "No se encuentra ningun Partido para el Id en la Base de datos"
        return jsonify(result)
    else:
        return jsonify(result)

@app.route("/partido", methods=['GET'])
def buscarTodosLosPartidos():
    result = controladorPartido.buscarTodosLosPartidos()
    if not result:
        return {"Resultado": "No se encuentran partidos en la base de datos!"}
    else:
        return jsonify(result)

@app.route("/partido/<string:idObject>", methods=['PUT'])
def actualizarPartido(idObject):
    validacion = controladorPartido.buscarPartido(idObject)
    if validacion == {}:
        json = {}
        json["message"] = "No se encuentra ningun Partido para el Id en la Base de datos"
        return jsonify(json)
    else:
        data = request.get_json()
        resultado = controladorPartido.actualizarPartido(idObject, data)
        return jsonify(resultado)

@app.route("/partido/<string:idObject>", methods=['DELETE'])
def eliminarPartido(idObject):
    validacion = controladorPartido.buscarPartido(idObject)
    if validacion == {}:
        json = {}
        json["message"] = "No se encuentra ningun Partido para el Id en la Base de datos"
        return jsonify(json)
    else:
        data = request.get_json()
        result = controladorPartido.eliminarPartido(idObject)
        return jsonify(result)

@app.route("/partido/All", methods=['DELETE'])
def eliminarTodosLosPartidos():
    validacion = controladorPartido.buscarTodosLosPartidos()
    if validacion == []:
        json = {}
        return {"Resultado": "No se encuentran Partidos en la base de datos!"}
    else:
        result = controladorPartido.eliminarTodosLosPartidos()
        return result

