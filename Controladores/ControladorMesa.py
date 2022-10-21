from repositorios.RepositorioMesa import RepositorioMesa
from Modelos.Mesa import Mesa

class ControladorMesa():
    def __init__(self):
        print("Entró al constructor de la clase Controlador Mesa")
        self.repositorioMesa = RepositorioMesa()

    def crearMesa(self, bodyRequest):
        print("Creando el estudiante....")
        nuevaMesa = Mesa(bodyRequest)
        print("estudiante a crear en base de datos: ", nuevaMesa.__dict__)
        self.repositorioMesa.save(nuevaMesa)
        return True

    def buscarMesa(self, idObject):
        print("Buscando la Mesa....", idObject)
        vMesa = Mesa(self.repositorioMesa.findById(idObject))
        return vMesa.__dict__

    def buscarTodasLasMesas(self):
        print("Buscando todos las Mesas en base de datos....")
        return self.repositorioMesa.findAll()

    def actualizarMesas(self, vmesa):
        mesaActual = Mesa(self.repositorioMesa.findById(vmesa["idObject"]))
        print("Actualizando el estudiante....", mesaActual)
        mesaActual.nombre = vmesa["nombre"]
        mesaActual.apellido = vmesa["apellido"]
        mesaActual.cedula = vmesa["cedula"]
        self.repositorioMesa.save(mesaActual)
        return True

    def eliminarMesa(self, idObject):
        print("Eliminando el mesa....", idObject)
        self.repositorioMesa.delete(idObject)
        return True