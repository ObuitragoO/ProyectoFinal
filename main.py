from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorCandidato import ControladorCandidato

app = Flask(__name__)
cors = CORS(app)

ControladorMesa = ControladorMesa()
"""ControladorCandidato = ControladorCandidato()"""


@app.route("/mesas",methods=['GET'])

def getMesa():
    json=ControladorMesa.index()
    return jsonify(json)

@app.route("/mesas",methods=['POST'])

def crearMesa():
    data = request.get_json()
    json=ControladorMesa.create(data)
    return jsonify(json)
@app.route("/mesas/<string:id>",methods=['GET'])
def traerMesa(id):
    json=ControladorMesa.show(id)
    return jsonify(json)
@app.route("/mesas/<string:id>",methods=['PUT'])

def modificarMesa(id):
    data = request.get_json()
    json=ControladorMesa.update(id,data)
    return jsonify(json)
@app.route("/estudiantes/<string:id>",methods=['DELETE'])
def eliminarMesa(id):
    json=ControladorMesa.delete(id)
    return jsonify(json)

@app.route("/saludo/",methods=['POST'])

def creacionMesa():
    getJsonO = request.get_json()
    print("el Body ",getJsonO)
    hostJson = request.host
    resultado = ControladorMesa.crearMesa()
    if(resultado):
        return {"resultado":"La Mesa se creo ok "}
    else:
        return {"resultado":"fallo"}

@app.route("/dos/",methods=['POST'])

def creacionCandidato():
    resultado = ControladorCandidato.creacionCandidato()
    return {"resultado":resultado}

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
