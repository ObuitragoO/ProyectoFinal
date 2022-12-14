from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from __main__ import app

from Controladores.ControladorCandidato import ControladorCandidato
controladorCandidato = ControladorCandidato()
from Controladores.ControladorPartido import ControladorPartido
controladorPartido = ControladorPartido ()

@app.route("/candidato", methods=['POST'])
def crearCandidato():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controladorCandidato.crearCandidato(requestBody)
    if result:
        return {"Resultado": "Candidato Creado!"}
    else:
        return {"Resultado": "Error al crear el candidato llamar a TI!"}

@app.route("/candidato/<string:idObject>", methods=['GET'])
def buscarCandidato(idObject):
    result = controladorCandidato.buscarCandidato(idObject)
    if result == {}:
        result = {}
        result["message"] = "No se encuentra ningun candidato para el Id en la Base de datos"
        return jsonify(result)
    else:
        return jsonify(result)

@app.route("/candidato", methods=['GET'])
def buscarTodasLosCandidatos():
    result = controladorCandidato.buscarTodosLosCandidatos()
    if not result:
        return {"Resultado": "No se encuentran candidatos en la base de datos!"}
    else:
        return jsonify(result)

@app.route("/candidato/<string:id>", methods=['PUT'])
def actualizarCandidato(id):
    validacion = controladorCandidato.buscarCandidato(id)
    if validacion == {}:
        json = {}
        json["message"] = "No se encuentra ningun candidato para el Id en la Base de datos"
        return jsonify(json)
    else:
        data = request.get_json()
        resultado = controladorCandidato.actualizarCandidato(id, data)
        return jsonify(resultado)

@app.route("/candidato/<string:idObject>", methods=['DELETE'])
def eliminarCandidato(idObject):
    validacion = controladorCandidato.buscarCandidato(idObject)
    if validacion == {}:
        json = {}
        json["message"] = "No se encuentra ningun candidato para el Id en la Base de datos"
        return jsonify(json)
    else:
        result = controladorCandidato.eliminarCandidato(idObject)
        return jsonify(result)
@app.route("/candidato/All", methods=['DELETE'])
def eliminarCandidatos():
    validacion = controladorCandidato.buscarTodosLosCandidatos()
    if validacion == []:
        json = {}
        return {"Resultado": "No se encuentran candidatos en la base de datos!"}
    else:
        result = controladorCandidato.eliminarTodosLosCandidato()
        return result

@app.route("/candidato/<string:id>/partido/<string:id_partido>",methods=['PUT'])
def asignarPartidoACandidato(id,id_partido):
    validacion1 = controladorCandidato.buscarCandidato(id)
    validacion2 = controladorPartido.buscarPartido(id_partido)
    if validacion1 == {} or validacion2 == {}:
        json = {}
        return {"Resultado": "No se encuentran el Candidato o el Partido indicados"}
    else:
        json = controladorCandidato.asignarPartido(id, id_partido)
        return jsonify(json)

@app.route("/candidato/cedula/<string:cedula>", methods=['GET'])
def buscarCandidatobyName(cedula):
    print(cedula)
    result = controladorCandidato.buscarCandidatobyCedula(cedula)
    if result == {}:
        result = {}
        print(result)
        return jsonify(result)
    else:
        print(result)
        return jsonify(result)