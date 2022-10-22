from repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Partido import Partido
class ControladorPartido():

    def __init__(self):
        print("Entró al constructor de la clase Controlador Partido")
        self.repositorioPartido = RepositorioPartido()

    def crearPartido(self, bodyRequest):
        print("Creando el Partido....")
        nuevoPartido = Partido(bodyRequest)
        print("Partido a crear en base de datos: ", nuevoPartido.__dict__)
        self.repositorioPartido.save(nuevoPartido)
        return True

    def buscarPartido(self, idObject):
        print("Buscando el Partido....", idObject)
        vPartido = Partido(self.repositorioPartido.findById(idObject))
        return vPartido.__dict__

    def buscarTodosLosPartidos(self):
        print("Buscando todos los Partidos en la base de datos....")
        return self.repositorioPartido.findAll()

    def actualizarPartido(self, vPartido):
        partidoActual = Partido(self.repositorioPartido.findById(vPartido["idObject"]))
        print("Actualizando el Partido....", partidoActual)
        partidoActual.id = vPartido["id"]
        partidoActual.nombre = vPartido["nombre"]
        partidoActual.lema = vPartido["lema"]
        self.repositorioPartido.save(partidoActual)
        return True

    def eliminarPartido(self, idObject):
        print("Eliminando el partido....", idObject)
        self.repositorioPartido.delete(idObject)
        return True