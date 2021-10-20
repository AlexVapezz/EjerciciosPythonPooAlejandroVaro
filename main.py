import random
import string

class Persona:

    __DNI = None
    __sexo = "M"
    __peso = 0
    __altura = 0
    __nombre = ""
    __edad = 0

    def __init__(self, DNI, sexo, peso, altura, nombre, edad):
        self.__DNI = DNI
        self.__sexo = sexo
        self.__peso = peso
        self.__altura = altura
        self.__nombre = nombre
        self.__edad = edad

    def introducirElementos(self):

        print("Introduzca su nombre:")
        self.__nombre=input()
        print("Introduzca su DNI")
        self.__DNI=input()
        print("Introduzca su peso kg")
        self.__peso=input()
        print("Introduzca su altura en metros")
        self.__altura = input()
        print("Introduzca su edad")
        self.__edad = input()

    def calcularIMC(self):

        weight = self.__peso
        height = self.__altura
        indicadorIMC = None

        if weight.isnumeric() and int(weight) >= 0:
            if height.isnumeric() and int(height) >= 0:
                IMC = (int(weight)/(int(height)**2))
            else:
                print("La altura introducida no es correcta")
                exit()
        else :
            print("El peso introducido no es correcto")
            exit()

        if IMC < 18.5:
            indicadorIMC = -1
        elif 18.5 < IMC < 25:
            indicadorIMC = 0
        elif 25 < IMC < 30:
            indicadorIMC = 1
        else:
            print("Error de IMC")
            exit()

        return indicadorIMC

    def esMayorDeEdad(self):

        age = self.__edad

        if age.isnumeric() and int(age) >= 0:
            if int(age) > 18:
                return True
            else:
                return False
        else:
            print("Edad introducida no valida")
            exit()


    def introducirSexo(self):

        print("Introduzca su sexo (M o H)")
        self.__sexo = input()
        gender = self.__sexo

        if gender == "M" or gender == "H":
            return gender
        else:
            gender = "M"
            return gender

    def toString(self):

        print("Los datos son los siguientes:")
        print("Nombre: " + self.__nombre)
        print("Edad: " + self.__edad)
        print("Genero: " + self.__sexo)
        print("Altura: " + self.__altura)
        print("Peso: " + self.__peso)

        indicadorMasaCorporal = self.calcularIMC()

        if indicadorMasaCorporal == -1:
            print("IMC: Delgado")
        elif indicadorMasaCorporal == 0:
            print("IMC: Normal")
        elif indicadorMasaCorporal == 1:
            print("IMC: Sobrepeso")
        else:
            print("Error")
            exit()

        mayoriaDeEdad = self.esMayorDeEdad()

        if mayoriaDeEdad:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")

        DNIGenerado = self.generaDNI()

        if len(str(DNIGenerado)) == 9:
            print("DNI: " + str(DNIGenerado))

    def generaDNI(self):

        while len(str(self.__DNI)) < 8:
            self.__DNI = random.randint(10000000, 99999999)

        if len(str(self.__DNI)) == 8:
            caracterRandom = random.choice(string.ascii_uppercase)
            self.__DNI = str(self.__DNI) + caracterRandom

            return self.__DNI

        else:
            print("Error en creacion de DNI")
            exit()

DNI1 = ""
print("Introduce tu genero (M o H)")
Genero1 = input()
print("Introduce tu peso en kg")
Peso1 = input()
print("Introduce tu altura en metros")
Altura1 = input()
print("Introduce tu nombre")
Nombre1 = input()
print("Introduce tu edad")
Edad1 = input()
Objeto1 = Persona(DNI1, Genero1, Peso1, Altura1, Nombre1, Edad1)
Objeto1.toString()

print("El genero, nombre y edad toman como valor por defecto el de la anterior persona")
print("Introduce tu peso en kg")
Peso2 = input()
print("Introduce tu altura en metros")
Altura2 = input()
Objeto2 = Persona(DNI1, Genero1, Peso2, Altura2, Nombre1, Edad1)
Objeto2.toString()

Genero3 = "M"
Peso3 = "0"
Altura3 = "0"
Nombre3 = ""
Edad3 = "0"
Objeto3 = Persona(DNI1, Genero3, Peso3, Altura3, Nombre3, Edad3)
Objeto3.toString()