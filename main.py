from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorPartido import ControladorPartido
from Controladores.ControladorResultado import ControladorResultado

ControladorMesa = ControladorMesa()
ControladorCandidato = ControladorCandidato()
ControladorPartido = ControladorPartido()
ControladorResultado = ControladorResultado()

app = Flask(__name__)
cors = CORS(app)

#Registro de endpoints para las funcionalidades de Mesa
@app.route("/mesa", methods=['POST'])
def crearMesa():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = ControladorMesa.crearMesa(requestBody)
    if result:
        return {"resultado": "Mesa Creada!"}
    else:
        return {"resultado": "Error al crear la mesa!"}

@app.route("/mesa/<string:idObject>", methods=['GET'])
def buscarMesa(idObject):
    result = ControladorMesa.buscarMesa(idObject)
    if result is None:
        return {"resultado": "No se encuentra la mesa en base de datos!"}
    else:
        return jsonify(result)

@app.route("/mesa", methods=['GET'])
def buscarTodosLasMesas():
    result = ControladorMesa.buscarTodasLasMesas()
    if not result:
        return {"resultado": "No se encuentran items en la base de datos!"}
    else:
        return jsonify(result)

@app.route("/mesa", methods=['PUT'])
def actualizarMesa():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = ControladorMesa.actualizarMesa(requestBody)
    if result:
        return {"resultado": "Mesa actualizada!"}
    else:
        return {"resultado": "Error al actualizar la Mesa!"}

@app.route("/mesa/<string:idObject>", methods=['DELETE'])
def eliminarMesa(idObject):
    result = ControladorMesa.eliminarMesa(idObject)
    if result:
        return {"resultado": "Mesa eliminada!"}
    else:
        return {"resultado": "Error al eliminar la Mesa!"}

# iniciar el servidor

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])




# comentarios por si falla

"""
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
@app.route("/mesas/<string:id>",methods=['DELETE'])
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


"""