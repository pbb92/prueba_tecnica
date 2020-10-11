from models.persona import Persona
from models.trabajador import Trabajador


def main():
    '''
        Pregunta 3: ¿Que diferencia hay entre self.nombre y la variable
        llamada nombre?

        self.nombre es una propiedad dentro del objeto Persona, es decir, solo
        existe dentro de esa clase  mientras que el scope de la variable nombre
        dependera de donde se genere, en este caso al generarse en una funcion,
        existira solo dentro de esta funcion. Si, por ejemplo, se crease la
        variable fuera de la función esta seria una variable global dentro de
        la clase main.py
    '''
    nombre = 'Alberto'
    persona_1 = Persona(nombre, 20)
    persona_1.presentation()

    # Si ahora no pasamos los valores departamento y puesto, por defector
    # usara "Data" y "Analyst respectivamente"
    trabajador_1 = Trabajador("Pepe", 30)
    trabajador_1.presentation()

    my_var_list = ["Andrea", "42", "Ventas", "Manager"]
    trabajador_2 = Trabajador(*my_var_list)
    trabajador_2.presentation()

    my_var_dict = {
        "nombre": "Andrea",
        "edad": 42,
        "departamento": "Ventas",
        "puesto": "Manager"
    }
    trabajador_3 = Trabajador(**my_var_dict)
    trabajador_3.presentation()


if __name__ == "__main__":
    main()
