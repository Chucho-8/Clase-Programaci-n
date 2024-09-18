from Alumno import Alumno #Del archivo alumno importame la clase alumno

def main():
    #jesus = Alumno()
    #print(jesus)
    jesus = Alumno("Jesús", "Cruz Hernández")
    print(jesus)

    jesus.saludar()
    jesus.adios()

    goku = Alumno("Goku", "")#Es un nuevo objeto de la clase alumno
    goku.saludar()#Ese objeto llama a la función saludar
    goku.adios()

if __name__ == "__main__":
    main()