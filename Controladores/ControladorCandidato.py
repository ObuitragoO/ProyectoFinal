from repositorios.RepositorioCandidato import RepositorioCandidato
from repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Candidato import Candidato
from Modelos.Partido import Partido

class ControladorCandidato():
    def __init__(self):
        print("Entró al constructor de la clase Controlador Candidato")
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioPartido = RepositorioPartido()

    def crearCandidato(self, bodyRequest):
        print("Creando el Candidato....")
        nuevoCandidato = Candidato(bodyRequest)
        print("Candidato a crear en base de datos: ", nuevoCandidato.__dict__)
        self.repositorioCandidato.save(nuevoCandidato)
        return True
    def buscarCandidato(self, idObject):
        print("Buscando el Candidato....", idObject)
        vCandidato = Candidato(self.repositorioCandidato.findById(idObject))
        return vCandidato.__dict__

    def buscarTodosLosCandidatos(self):
        print("Buscando todos los Candidatos en base de datos....")
        return self.repositorioCandidato.findAll()


    def actualizarCandidato(self, id, vCandidato):
        candidatoActual = Candidato(self.repositorioCandidato.findById(id))
        print("Actualizando el candidato....", candidatoActual)
        candidatoActual.cedula = vCandidato["cedula"]
        candidatoActual.numero_resolucion = vCandidato["numero_resolucion"]
        candidatoActual.nombre = vCandidato["nombre"]
        candidatoActual.apellido = vCandidato["apellido"]
        return self.repositorioCandidato.save(candidatoActual)

    def eliminarCandidato(self, idObject):
        print("Eliminando el candidato....", idObject)
        return self.repositorioCandidato.delete(idObject)

    def eliminarTodosLosCandidato(self):
        print("Eliminando todos los candidato....")
        return self.repositorioCandidato.deleteAll()

    """
        Relación Partido y Candidato
    """
    def asignarPartido(self, id, id_partido):
        candidatoActual = Candidato(self.repositorioCandidato.findById(id))
        partidoActual = Partido(self.repositorioPartido.findById(id_partido))
        candidatoActual.partido = partidoActual
        return self.repositorioCandidato.save(candidatoActual)

