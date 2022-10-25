from repositorios.RepositorioResultado import RepositorioResultado
from Modelos.Resultado import Resultado

class ControladorResultado():

    def __init__(self):
        print("Entró al constructor de la clase Controlador Resultado")
        self.repositorioResultado = RepositorioResultado()

    def crearResultado(self, bodyRequest):
        print("Creando el Resultado....")
        nuevoResultado = Resultado(bodyRequest)
        print("Rersultado a crear en base de datos: ", nuevoResultado.__dict__)
        self.repositorioResultado.save(nuevoResultado)
        return True

    def buscarResultado(self, idObject):
        print("Buscando el Resultado....", idObject)
        vResultado = Resultado(self.repositorioResultado.findById(idObject))
        return vResultado.__dict__

    def buscarTodosLosResultados(self):
        print("Buscando todos los Partidos en la base de datos....")
        return self.repositorioResultado.findAll()

    def actualizarResultado(self, id, vPartido):
        ResultadoActual = Resultado(self.repositorioResultado.findById(id))
        print("Actualizando el partido....", ResultadoActual)
        ResultadoActual.numero_mesa = vPartido["numero_mesa"]
        ResultadoActual.cedula_candidato = vPartido["cedula_candidato"]
        ResultadoActual.numero_votos = vPartido["numero_votos"]
        return self.repositorioResultado.save(ResultadoActual)

    def eliminarResultado(self, idObject):
        print("Eliminando el resultado....", idObject)
        return self.repositorioResultado.delete(idObject)

    def eliminarTodosLosResultados(self):
        print("Eliminando todas los Resultados....")
        return self.repositorioResultado.deleteAll()

