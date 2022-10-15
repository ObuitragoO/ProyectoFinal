class ControladorPartido():

    def __init__(self):
        print("Entro al constructor de la clase controlador Partido")

    def crearPartido(self):
        print("logica de crear Partido politico")
        return True

    def index(self):
        print("Listar todos los Partidos politicos ")

    def create(self, elPartido):
        print("Crear un Partido politico")

    def show(self, id):
        print("Mostrando un Partido politico con id ", id)

    def update(self, id, elPartido):
        print("Actualizando Partido politico con id ", id)

    def delete(self, id):
        print("Elimiando Partido politico con id ", id)