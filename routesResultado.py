from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from __main__ import app

from Controladores.ControladorResultado import ControladorResultado
controladorResultado = ControladorResultado()
from Controladores.ControladorCandidato import ControladorCandidato
controladorCandidato = ControladorCandidato()
from Controladores.ControladorMesa import ControladorMesa
controladorMesa = ControladorMesa()


# Registro de endpoints para las funcionalidades de Resultado

@app.route("/resultado/candidato/<string:id_candidato>/mesa/<string:id_mesa>",methods=['POST'])
def crearResultado(id_candidato,id_mesa):
    validacion1 = controladorMesa.buscarMesa(id_mesa)
    validacion2 = controladorCandidato.buscarCandidato(id_candidato)
    if validacion1 == {} or validacion2 == {}:
        json = {}
        return {"Resultado": "No se encuentran la Mesa o el Candidato indicados"}
    else:
        data = request.get_json()
        result = controladorResultado.crearResultado(data, id_candidato, id_mesa)
        return jsonify(result)

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

@app.route("/resultado/<string:id_resultado>/candidato/<string:id_candidato>/mesa/<string:id_mesa>",methods=['PUT'])
def actualizarResultado(id_resultado,id_candidato,id_mesa):
    validacion1 = controladorResultado.buscarResultado(id_resultado)
    validacion2 = controladorMesa.buscarMesa(id_mesa)
    validacion3 = controladorCandidato.buscarCandidato(id_candidato)
    if validacion1 == {} or validacion2 == {} or validacion3 == {}:
        json = {}
        return {"Resultado": "No se encuentran los datos indicados indicados"}
    else:
        data = request.get_json()
        json=controladorResultado.actualizarResultado(id_resultado,data,id_candidato,id_mesa)
        return jsonify(json)

@app.route("/resultado/<string:idObject>", methods=['DELETE'])
def eliminarResultado(idObject):
    validacion = controladorResultado.buscarResultado(idObject)
    if validacion == {}:
        json = {}
        json["message"] = "No se encuentra ningun Resultado para el Id en la Base de datos"
        return jsonify(json)
    else:
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
