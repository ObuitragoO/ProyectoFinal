from repositorios.RepositorioCandidato import RepositorioCandidato
from Modelos.Candidato import Candidato


class ControladorCandidato():
    def __init__(self):
        print("Entró al constructor de la clase Controlador Candidato")
        self.repositorioCandidato = RepositorioCandidato()

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


    def actualizarCandidato(self, vCandidato):
        candidatoActual = Candidato(self.repositorioCandidato.findById(vCandidato["idObject"]))
        print("Actualizando el candidato....", candidatoActual)
        candidatoActual.cedula = vCandidato["cedula"]
        candidatoActual.numero_resolucion = vCandidato["numero_resolucion"]
        candidatoActual.nombre = vCandidato["nombre"]
        candidatoActual.apellido = vCandidato["apellido"]
        self.repositorioCandidato.save(candidatoActual)
        return True

    def eliminarCandidato(self, idObject):
        print("Eliminando el candidato....", idObject)
        self.repositorioCandidato.delete(idObject)
        return True
