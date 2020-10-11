from models.persona import Persona


class Trabajador(Persona):
    def __init__(self, nombre, edad, departamento, puesto):
        super().__init__(nombre, edad)
        self.departamento = departamento
        self.puesto = puesto
