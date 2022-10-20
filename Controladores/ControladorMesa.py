from repositorios.RepositorioMesa import RepositorioMesa
from Modelos.Mesa import Mesa

class ControladorMesa():
    def __init__(self):
        print("Entró al constructor de la clase ControladorMesa")
        self.repositorioMesa = RepositorioMesa()

    def crearMesa(self, bodyRequest):
        print("Creando el mesa....")
        nuevaMesa = Mesa(bodyRequest)
        print("estudiante a crear en base de datos: ", nuevaMesa.__dict__)
        self.repositorioMesa.save(nuevaMesa)
        return True

    def buscarMesa(self, idObject):
        print("Buscando la mesa ....", idObject)
        estudiante = Mesa(self.repositorioMesa.findById(idObject))
        return estudiante.__dict__

    def buscarTodasLasMesas(self):
        print("Buscando todos los mesas en base de datos....")
        return self.repositorioMesa.findAll()

    def actualizarMesa(self, mesa):
        mesaActual = mesa(self.repositorioMesa.findById(mesa["idObject"]))
        print("Actualizando la mesa....", mesaActual)
        mesaActual.nombre = mesa["nombre"]
        mesaActual.apellido = mesa["apellido"]
        mesaActual.cedula = mesa["cedula"]
        self.repositorioEstudiante.save(mesaActual)
        return True

    def eliminarMesa(self, idObject):
        print("Eliminando la mesa....", idObject)
        self.repositorioMesa.delete(idObject)
        return True


"""
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

"""