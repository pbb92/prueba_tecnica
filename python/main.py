from models.persona import Persona
from models.trabajador import Trabajador


def main():
    nombre = 'Alberto'
    persona_1 = Persona(nombre, 20)
    persona_1.presentation()

    trabajador_1 = Trabajador("Pepe", 30, "Data", "Analyst")
    trabajador_1.presentation()


if __name__ == "__main__":
    main()
