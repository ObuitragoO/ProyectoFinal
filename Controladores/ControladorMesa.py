class ControladorMesa():

    def __init__(self):
        print("Creando Controlador Mesa")

    def crearMesa(self):
        print("logica de crear Mesa")
        return True

    def index(self):
        print("Listar todas las mesas ")

    def create(self, laMesa):
        print("Crear una mesa")

    def show(self, id):
        print("Mostrando un mesa con id ", id)

    def update(self, id, laMesa):
        print("Actualizando mesa con id ", id)

    def delete(self, id):
        print("Elimiando mesa con id ", id)