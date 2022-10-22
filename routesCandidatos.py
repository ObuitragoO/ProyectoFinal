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
        return {"resultado": "Candidato Creado!"}
    else:
        return {"resultado": "Error al crear el candidato llamar a TI!"}

@app.route("/candidato/<string:idObject>", methods=['GET'])
def buscarCandidato(idObject):
    result = controladorCandidato.buscarCandidato(idObject)
    if result is None:
        return {"resultado": "No se encuentra el candidato en base de datos!"}
    else:
        return jsonify(result)

@app.route("/candidato", methods=['GET'])
def buscarTodasLosCandidatos():
    result = controladorCandidato.buscarTodosLosCandidatos()
    if not result:
        return {"resultado": "No se encuentran candidatos en la base de datos!"}
    else:
        return jsonify(result)

@app.route("/candidato", methods=['PUT'])
def actualizarCandidato():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controladorCandidato.actualizarCandidato(requestBody)
    if result:
        return {"resultado": "Candidato actualizado!"}
    else:
        return {"resultado": "Error al actualizar el Candidato!"}

@app.route("/candidato/<string:idObject>", methods=['DELETE'])
def eliminarCandidato(idObject):
    result = controladorCandidato.eliminarCandidato(idObject)
    if result:
        return {"resultado": "Candidato eliminada!"}
    else:
        return {"resultado": "Error al eliminar la candidato!"}

