## Menú interactivo ##

from pizza import Pizza
from tiempo import estimar_tiempo

def mostrar_menu():
    pizza = Pizza()
    opciones_masa = ["Tradicional", "Delgada", "Con Bordes de Queso"]
    opciones_salsa = ["Tomate", "Alfredo", "Barbecue", "Pesto"]
    ingredientes_disponibles = ["Tomate", "Champiñones", "Aceituna","Cebolla", "Pollo", "Jamón", "Carne", "Tocino", "Queso"]

    while True:
        print("""\n - MENÚ - PERSONALICEMOS LA PIZZA -
1. Cambiar masa
2. Cambiar salsa
3. Agregar ingrediente
4. Eliminar ingrediente
5. Ver pizza actual
6. Confirmar y ordenar
7. Salir
        """)
        opcion = input("Elige una opción, cuando así lo indique: ")

        if opcion == "1":
            print("Opciones de masa:", opciones_masa)
            masa = input("Selecciona la masa (sólo una opción): ").strip().title()
            if masa in opciones_masa:
                pizza.cambiar_masa(masa)
            else:
                print("Masa no válida.")
        elif opcion == "2":
            print("Opciones de salsa:", opciones_salsa)
            salsa = input("Selecciona la salsa (sólo una opción): ").strip().title()
            if salsa in opciones_salsa:
                pizza.cambiar_salsa(salsa)
            else:
                print("Salsa no válida.")
        elif opcion == "3":
            print("Ingredientes disponibles:", ingredientes_disponibles)
            entrada = input("Escribe los ingredientes que deseas agregar, separados por comas: ")
            lista_ingresados = [x.strip().title() for x in entrada.split(",")]

            for ing in lista_ingresados:
                if ing in ingredientes_disponibles:
                    pizza.agregar_ingrediente(ing)
                    print(f"El ingrediente '{ing}' ha sido agregado.")
                else:
                    print(f"El ingrediente '{ing}' no es válido.")
        elif opcion == "4":
            ing = input("¿Qué ingrediente quieres eliminar?: ")
            pizza.eliminar_ingrediente(ing)
        elif opcion == "5":
            pizza.mostrar()
        elif opcion == "6":
            pizza.mostrar()
            tiempo = estimar_tiempo(len(pizza.ingredientes))
            print(f"Tu pizza estará lista en aproximadamente {tiempo} minutos.")
            confirmar = input("¿Deseas confirmar la orden? (sí/no): ").strip().lower()
            if confirmar == "sí":
                print("¡Orden confirmada! Gracias por tu compra :)")
                break
        elif opcion == "7":
            print("Que disfrutes la zappi y ¡Vuelva pronto!")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")