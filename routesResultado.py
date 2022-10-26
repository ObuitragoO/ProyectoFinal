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
    if result == {}:
        result = {}
        result["message"] = "No se encuentra ningun Resultado para el Id en la Base de datos"
        return jsonify(result)
    else:
        return jsonify(result)

@app.route("/resultado", methods=['GET'])
def buscarTodosLosResultados():
    result = controladorResultado.buscarTodosLosResultados()
    if not result:
        return {"resultado": "No se encuentran Resultados en la base de datos!"}
    else:
        return jsonify(result)

@app.route("/resultado/<string:idObject>", methods=['PUT'])
def actualizarResultado(idObject):
    validacion = controladorResultado.buscarResultado(idObject)
    if validacion == {}:
        json = {}
        json["message"] = "No se encuentra ningun Resultado para el Id en la Base de datos"
        return jsonify(json)
    else:
        data = request.get_json()
        resultado = controladorResultado.actualizarResultado(idObject, data)
        return jsonify(resultado)

@app.route("/resultado/<string:idObject>", methods=['DELETE'])
def eliminarResultado(idObject):
    validacion = controladorResultado.buscarResultado(idObject)
    if validacion == {}:
        json = {}
        json["message"] = "No se encuentra ningun Resultado para el Id en la Base de datos"
        return jsonify(json)
    else:
        data = request.get_json()
        result = controladorResultado.eliminarResultado(idObject)
        return jsonify(result)

@app.route("/resultado/All", methods=['DELETE'])
def eliminarTodosLosResultados():
    validacion = controladorResultado.buscarTodosLosResultados()
    if validacion == []:
        json = {}
        return {"Resultado": "No se encuentran Resultados en la base de datos!"}
    else:
        result = controladorResultado.eliminarTodosLosResultados()
        return result
