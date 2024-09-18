

class Alumno:#así se define una clase en python
    def __init__(self,nombre,apellido):#tiene un constructor
        #self.nombre = "Sin definir"#Propiedades
        #self.apellido = "Sin definir"
        self.nombre = nombre
        self.apellido = apellido

    def saludar(self):#Dame acceso a l amisma clase donde estoy en la propiedad nombre
        print(f"Hola, mi nombre es {self.nombre}, que tengas un buen día")#f al inicio, luego el self que se crea en el constructor
        
    def adios(self):
        print(f"Me despido, soy {self.nombre}")

    def __str__(self):#regresa una cadena de caracteres del objetoTiene como se escribe
        return self.nombre + " " + self.apellido

