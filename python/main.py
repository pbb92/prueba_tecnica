from models.persona import Persona


def main():
    nombre = 'Alberto'
    persona_1 = Persona(nombre, 20)
    persona_1.presentation()


if __name__ == "__main__":
    main()
