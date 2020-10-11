from models.persona import Persona


class Trabajador(Persona):
    def __init__(self, nombre, edad, departamento="Data", puesto="Analyst"):
        super().__init__(nombre, edad)
        self.departamento = departamento
        self.puesto = puesto

    def presentation(self):
        super().presentation()
        print(f"Trabajo en el departamento: {self.departamento} y mi puesto es {self.puesto}")
