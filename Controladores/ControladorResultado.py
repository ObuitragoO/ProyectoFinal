class ControladorResultado():

    def __init__(self):
        print("Entro al constructor de la clase controlador Resultado")


    def crearResultado(self):
        print("logica de crear Resultado")
        return True

    def index(self):
        print("Listar todos los Resultado ")

    def create(self, elResultado):
        print("Crear un Resultado")

    def show(self, id):
        print("Mostrando un Resultado con id ", id)

    def update(self, id, elResultado):
        print("Actualizando Resultado con id ", id)

    def delete(self, id):
        print("Elimiando Resultado con id ", id)