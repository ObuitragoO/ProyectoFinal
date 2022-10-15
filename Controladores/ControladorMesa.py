from Modelos.Mesa import Mesa

class ControladorMesa():

    def __init__(self):
        print("Creando Controlador Mesa")

    def index(self):
        print("Listar todas las mesas ")
        unaMesa = {
            "_id": "1",
            "Mesa": "MESA1",
            "Colegio": "Robert F kennedy"
        }
        return unaMesa
    def create(self, infoMesa):
        print("Crear una mesa")
        laMesa = Mesa(infoMesa)
        return laMesa.__dict__

    def show(self, id):
        print("Mostrando un mesa con id ", id)
        unaMesa = {
            "_id": "2",
            "Mesa": "MESA2",
            "Colegio": "kennedy"
        }
        return unaMesa
    def update(self, id, infoMesa):
        print("Actualizando mesa con id ", id)
        laMesa = Mesa(infoMesa)
        return laMesa.__dict__

    def delete(self, id):
        print("Elimiando mesa con id ", id)
        return {"deleted_count": 1}