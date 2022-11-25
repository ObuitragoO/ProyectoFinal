from repositorios.RepositorioMesa import RepositorioMesa
from Modelos.Mesa import Mesa


class ControladorMesa():
    def __init__(self):
        print("Entró al constructor de la clase Controlador Mesa")
        self.repositorioMesa = RepositorioMesa()

    def crearMesa(self, bodyRequest):
        print("Creando el estudiante....")
        nuevaMesa = Mesa(bodyRequest)
        print("Mesa a crear en base de datos: ", nuevaMesa.__dict__)
        self.repositorioMesa.save(nuevaMesa)
        return True

    def buscarMesa(self, idObject):
        print("Buscando la Mesa....", idObject)
        vMesa = Mesa(self.repositorioMesa.findById(idObject))
        return vMesa.__dict__

    def buscarTodasLasMesas(self):
        print("Buscando todos las Mesas en base de datos....")
        return self.repositorioMesa.findAll()

    def actualizarMesas(self, id, vmesa):
        mesaActual = Mesa(self.repositorioMesa.findById(id))
        print("Actualizando el estudiante....", mesaActual)
        mesaActual.numero = vmesa["numero"]
        mesaActual.cantidad_inscritos = vmesa["cantidad_inscritos"]
        return self.repositorioMesa.save(mesaActual)

    def eliminarMesa(self, idObject):
        print("Eliminando el mesa....", idObject)
        return self.repositorioMesa.delete(idObject)


    def eliminarTodasLasMesas(self):
        print("Eliminando todas las mesas....")
        return self.repositorioMesa.deleteAll()

    def buscarMesabyNumero(self, numero):
        print("Buscando la mesa....", numero)
        vMesa = Mesa(self.repositorioMesa.findByNumero(numero))
        return vMesa.__dict__
