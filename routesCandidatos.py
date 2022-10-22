from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

from Controladores.ControladorCandidato import ControladorCandidato
from __main__ import app

controladorCandidato = ControladorCandidato()

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
    if result is None:
        return {"Resultado": "No se encuentra el candidato en base de datos!"}
    else:
        return jsonify(result)

@app.route("/candidato", methods=['GET'])
def buscarTodasLosCandidatos():
    result = controladorCandidato.buscarTodosLosCandidatos()
    if not result:
        return {"Resultado": "No se encuentran candidatos en la base de datos!"}
    else:
        return jsonify(result)

@app.route("/candidato", methods=['PUT'])
def actualizarCandidato():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controladorCandidato.actualizarCandidato(requestBody)
    if result:
        return {"Resultado": "Candidato actualizado!"}
    else:
        return {"Resultado": "Error al actualizar el Candidato!"}

@app.route("/candidato/<string:idObject>", methods=['DELETE'])
def eliminarCandidato(idObject):
    result = controladorCandidato.eliminarCandidato(idObject)
    if result:
        return {"Resultado": "Candidato eliminada!"}
    else:
        return {"Resultado": "Error al eliminar el candidato!"}

