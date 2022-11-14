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
    if result == {}:
        result = {}
        result["message"] = "No se encuentra ninguna Mesa para el Id en la Base de datos"
        return jsonify(result)
    else:
        return jsonify(result)

@app.route("/mesa", methods=['GET'])
def buscarTodasLasMesas():
    result = controladorMesa.buscarTodasLasMesas()
    if not result:
        return {"Resultado": "No se encuentran mesas en la base de datos!"}
    else:
        return jsonify(result)

@app.route("/mesa/<string:idObject>", methods=['PUT'])
def actualizarMesa(idObject):
    validacion = controladorMesa.buscarMesa(idObject)
    if validacion == {}:
        json = {}
        json["message"] = "No se encuentra ninguna Mesa para el Id en la Base de datos"
        return jsonify(json)
    else:
        data = request.get_json()
        resultado = controladorMesa.actualizarMesas(idObject, data)
        return jsonify(resultado)

@app.route("/mesa/<string:idObject>", methods=['DELETE'])
def eliminarMesa(idObject):
    validacion = controladorMesa.buscarMesa(idObject)
    if validacion == {}:
        json = {}
        json["message"] = "No se encuentra ninguna Mesa para el Id en la Base de datos"
        return jsonify(json)
    else:
        result = controladorMesa.eliminarMesa(idObject)
        return jsonify(result)

@app.route("/mesa/All", methods=['DELETE'])
def eliminarTodasLasmesas():
    validacion = controladorMesa.buscarTodasLasMesas()
    if validacion == []:
        json = {}
        return {"Resultado": "No se encuentran mesas en la base de datos!"}
    else:
        result = controladorMesa.eliminarTodasLasMesas()
        return result


