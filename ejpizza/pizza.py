
## estructura de la pizza ##

class Pizza:
    def __init__(self):
        self.masa = "Tradicional"
        self.salsa = "Tomate"
        self.ingredientes = []

    def cambiar_masa(self, nueva_masa):
        self.masa = nueva_masa

    def cambiar_salsa(self, nueva_salsa):
        self.salsa = nueva_salsa

    def agregar_ingrediente(self, ing):
        if ing not in self.ingredientes:
            self.ingredientes.append(ing)

    def eliminar_ingrediente(self, ing):
        if ing in self.ingredientes:
            self.ingredientes.remove(ing)

    def mostrar(self):
        print(f"\nTu pizza actual tiene:")
        print(f" - Masa: {self.masa}")
        print(f" - Salsa: {self.salsa}")
        print(f" - Ingredientes: {', '.join(self.ingredientes) if self.ingredientes else 'Sin ingredientes'}")
