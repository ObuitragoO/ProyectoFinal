from repositorios.RepositorioResultado import RepositorioResultado
from repositorios.RepositorioMesa import RepositorioMesa
from repositorios.RepositorioCandidato import RepositorioCandidato
from Modelos.Resultado import Resultado
from Modelos.Mesa import Mesa
from Modelos.Candidato import Candidato

class ControladorResultado():

    def __init__(self):
        print("Entró al constructor de la clase Controlador Resultado")
        self.repositorioResultado = RepositorioResultado()
        self.repositorioMesa = RepositorioMesa()
        self.repositorioCandidato = RepositorioCandidato()
    """
    Asignacion candidato y mesa a resultado
    """
    def crearResultado(self, infoResultado,id_candidato,id_mesa):
        nuevoResultado = Resultado(infoResultado)
        print("Rersultado a crear en base de datos: ", nuevoResultado.__dict__)
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        nuevoResultado.candidato = elCandidato
        nuevoResultado.mesa = laMesa
        return self.repositorioResultado.save(nuevoResultado)

    def buscarResultado(self, idObject):
        print("Buscando el Resultado....", idObject)
        vResultado = Resultado(self.repositorioResultado.findById(idObject))
        return vResultado.__dict__

    def buscarTodosLosResultados(self):
        print("Buscando todos los Partidos en la base de datos....")
        return self.repositorioResultado.findAll()

    """
    Modificación de resultado (candidato y mesa)
    """
    def actualizarResultado(self, id, infoResultado, id_candidato,id_mesa):
        elResultado = Resultado(self.repositorioResultado.findById(id))
        elResultado.numero_votos = infoResultado["numero_votos"]
        elCandidato =Candidato(self.repositorioCandidato.findById(id_candidato))
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        elResultado.candidato = elCandidato
        elResultado.mesa = laMesa
        return self.repositorioResultado.save(elResultado)

    def eliminarResultado(self, idObject):
        print("Eliminando el resultado....", idObject)
        return self.repositorioResultado.delete(idObject)

    def eliminarTodosLosResultados(self):
        print("Eliminando todas los Resultados....")
        return self.repositorioResultado.deleteAll()

