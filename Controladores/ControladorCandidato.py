class ControladorCandidato():

    def __init__(self):
        print("Entro al constructor de la clase controlador del Candidato")

    def crearCandidato(self):
        print("logica de crear Candidato")
        return True

    def index(self):
        print("Listar todos los candidatos ")

    def create(self, elCandidato):
        print("Crear un Candidato")

    def show(self, id):
        print("Mostrando un Candidato con id ", id)

    def update(self, id, elCandidato):
        print("Actualizando Candidato con id ", id)

    def delete(self, id):
        print("Elimiando candidato con id ", id)