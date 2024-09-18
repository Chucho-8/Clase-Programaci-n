
class Padre():
    def __init__(self):
        print("Hola, soy padre")

    def trabajar(self):
        print("Hola, estoy trabajando")

class Madre():
    def __init__(self):
        print("Hola, soy madre")

    def cocinar(self):
        print("Hola, estoy cocinando")

#class Hijo():#si queremos que Hijo herede todo lo de padre, se pone entre parentesis
class Hijo(Padre):    
    def __init__(self):
        #para que todo funcione se debe ocupar super().__init__() es quien hace que se pueda heredar todo lo de una clase en otra clase
        ###super().__init__()#Es para heredar
        #Constructor de la super clase, pero sólo hereda de una clase
        Padre.__init__(self)#Se le está heredando __init__(self)
        Madre.__init__(self)
        print("Hola, soy hijo")

def main():
    hijo = Hijo()
    hijo.trabajar()#hijo no tinee trabajar, pero lo tiene el Padre, 
    #Despues de heredar de padre, hijo ya tambien tiene el metodo/función trabajar


if __name__ ==  "__main__":
    main()