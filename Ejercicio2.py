class Electrodomestico():

    _precio = 100
    _color = "blanco"
    _consumo_energetico = "F"
    _peso = 5

    def __init__(self, precio, color, consumo_energetico, peso):
        self._precio = precio
        self._color = color
        self._consumo_energetico = consumo_energetico
        self._peso = peso

    def comprobarConsumoEnergetico(self):

        conEner = self._consumo_energetico

        if conEner in ["A", "B", "C", "D", "E", "F"]:
            return conEner
        else:
            conEner = "F"
            self._consumo_energetico = conEner

    def comprobarColor(self):

        colorComp = self._color

        if colorComp in ["blanco", "negro", "rojo", "azul", "gris"]:
            return colorComp
        else:
            colorComp = "blanco"
            self._color = colorComp

    def precioFinal(self):

        self.comprobarColor()
        self.comprobarConsumoEnergetico()
        precioInit = self._precio
        conEnerInit = self._consumo_energetico
        pesoInit = self._peso

        if conEnerInit == "A":
            precioInit = int(precioInit) + 100
        elif conEnerInit == "B":
            precioInit = int(precioInit) + 80
        elif conEnerInit == "C":
            precioInit = int(precioInit) + 60
        elif conEnerInit == "D":
            precioInit = int(precioInit) + 50
        elif conEnerInit == "E":
            precioInit = int(precioInit) + 30
        elif conEnerInit == "F":
            precioInit = int(precioInit) + 10
        else:
            print("Valo energetico no valido")
            exit()

        if 0 <= int(pesoInit) <= 19:
            precFin = int(precioInit) + 10
        elif 20 <= int(pesoInit) <= 49:
            precFin = int(precioInit) + 50
        elif 50 <= int(pesoInit) <= 79:
            precFin = int(precioInit) + 80
        elif int(pesoInit) >= 80:
            precFin = int(precioInit) + 100
        else:
            print("Peso no valido")
            exit()

        return precFin



class Lavadora(Electrodomestico):

    _carga = 5

    def __init__(self, precio, color, consumo_energetico, peso, carga):
        self._precio = precio
        self._color = color
        self._consumo_energetico = consumo_energetico
        self._peso = peso
        self._carga = carga

    def precioFinal(self):

        Electrodomestico.comprobarConsumoEnergetico(self)
        Electrodomestico.comprobarColor(self)
        precioInit = self._precio
        baseCharge = self._carga
        conEnerInit = self._consumo_energetico
        pesoInit = self._peso

        if conEnerInit == "A":
            precioInit = int(precioInit) + 100
        elif conEnerInit == "B":
            precioInit = int(precioInit) + 80
        elif conEnerInit == "C":
            precioInit = int(precioInit) + 60
        elif conEnerInit == "D":
            precioInit = int(precioInit) + 50
        elif conEnerInit == "E":
            precioInit = int(precioInit) + 30
        elif conEnerInit == "F":
            precioInit = int(precioInit) + 10
        else:
            print("Valo energetico no valido")
            exit()

        if 0 <= int(pesoInit) <= 19:
            precioInit = int(precioInit) + 10
        elif 20 <= int(pesoInit) <= 49:
            precioInit = int(precioInit) + 50
        elif 50 <= int(pesoInit) <= 79:
            precioInit = int(precioInit) + 80
        elif int(pesoInit) >= 80:
            precioInit = int(precioInit) + 100
        else:
            print("Peso no valido")
            exit()

        if int(baseCharge) > 30:
            precFin = int(precioInit) + 50
        else:
            precFin = precioInit

        return precFin


class Television(Electrodomestico):

    _resolucion = 20
    _fourK = False

    def __init__(self, precio, color, consumo_energetico, peso, resolucion, fourK):
        self._precio = precio
        self._color = color
        self._consumo_energetico = consumo_energetico
        self._peso = peso
        self._resolucion = resolucion
        self._fourK = fourK

    def precioFinal(self):

        Electrodomestico.comprobarConsumoEnergetico(self)
        Electrodomestico.comprobarColor(self)
        baseResolution = self._resolucion
        baseFourK = self._fourK
        precioInit = self._precio
        conEnerInit = self._consumo_energetico
        pesoInit = self._peso

        if conEnerInit == "A":
            precioInit = int(precioInit) + 100
        elif conEnerInit == "B":
            precioInit = int(precioInit) + 80
        elif conEnerInit == "C":
            precioInit = int(precioInit) + 60
        elif conEnerInit == "D":
            precioInit = int(precioInit) + 50
        elif conEnerInit == "E":
            precioInit = int(precioInit) + 30
        elif conEnerInit == "F":
            precioInit = int(precioInit) + 10
        else:
            print("Valo energetico no valido")
            exit()

        if 0 <= int(pesoInit) <= 19:
            precioInit = int(precioInit) + 10
        elif 20 <= int(pesoInit) <= 49:
            precioInit = int(precioInit) + 50
        elif 50 <= int(pesoInit) <= 79:
            precioInit = int(precioInit) + 80
        elif int(pesoInit) >= 80:
            precioInit = int(precioInit) + 100
        else:
            print("Peso no valido")
            exit()

        if int(baseResolution) > 40 and baseFourK == True:
            precFin = int(precioInit) + 50
        else:
            precFin = precioInit

            return precFin


def ejecutarScript():

    arrayElect = []
    sumaElect = 0
    sumaLavad = 0
    sumaTV = 0

    print("¿Cuantos electrodomésticos desea introducir?")
    NumElect = input()

    if NumElect.isnumeric() and int(NumElect) > 0:
        for i in range(int(NumElect)):

            print("Introduzca el " + str(i+1) + " electrodomestico (Electrodomestico, lavadora o television)")
            ElectType = input()

            if ElectType in ["Electrodomestico", "electrodomestico", "ELECTRODOMESTICO"]:

                precio = getPrecioInit()
                color = getColorInit()
                consumo = getConsumoInit()
                peso = getPesoInit()

                Elect = Electrodomestico(precio, color, consumo, peso)
                precioFinalElect = Elect.precioFinal()
                arrayElect.append(precioFinalElect)
                sumaElect += precioFinalElect

                print("El precio del electrodomestico es de " + str(precioFinalElect))

            elif ElectType in ["Lavadora", "lavadora", "LAVADORA"]:

                precio = getPrecioInit()
                color = getColorInit()
                consumo = getConsumoInit()
                peso = getPesoInit()
                carga = getCargaInit()

                Lavad = Lavadora(precio, color, consumo, peso, carga)
                precioFinalLav = Lavad.precioFinal()
                arrayElect.append(precioFinalLav)
                sumaLavad += precioFinalLav
                sumaElect += precioFinalLav

                print("El precio de la lavadora es de " + str(precioFinalLav))

            elif ElectType in ["Television", "television", "TELEVISION", "TV", "tv", "Tv"]:

                precio = getPrecioInit()
                color = getColorInit()
                consumo = getConsumoInit()
                peso = getPesoInit()
                resolucion = getResolucionInit()
                fourk = getFourKInit()

                Telev = Television(precio, color, consumo, peso, resolucion, fourk)
                precioFinalTV = Telev.precioFinal()
                arrayElect.append(precioFinalTV)
                sumaTV += precioFinalTV
                sumaElect += precioFinalTV

                print("El precio de la television es de " + str(precioFinalTV))

            else:

                print("El valor introducido no es valido")
                exit()

        arrayToString = ' '.join(map(str, arrayElect))
        print("La lista de todos los electrodomesticos es la siguiente: " + arrayToString)
        print("El precio total de las lavadoras ha sido: " + str(sumaLavad))
        print("El precio total de los televisores ha sido: " + str(sumaTV))
        print("El precio total de los electrodomesticos ha sido: " + str(sumaElect))

    else:

        print("Error, el valor no es valido")
        exit()


def getPrecioInit():

    print("Introduzca el precio")
    precioInit = input()

    if precioInit.isnumeric() and int(precioInit) > 0:
        return precioInit
    else:
        print("El precio introducido no es correcto")
        exit()


def getColorInit():

    print("Introduzca el color (blanco, negro, rojo, azul o gris)")
    colorInit = input()

    return colorInit


def getConsumoInit():

    print("Introduzca el consumo energetico (A, B, C, D, E, F)")
    consumoInit = input()

    return consumoInit


def getPesoInit():

    print("Introduzca el peso en kg")
    pesoInit = input()

    if pesoInit.isnumeric() and int(pesoInit) > 0:
        return pesoInit
    else:
        print("El peso introducido no es correcto")
        exit()


def getCargaInit():

    print("Introduzca la carga en kg")
    cargaInit = input()

    if cargaInit.isnumeric() and int(cargaInit) > 0:
        return cargaInit
    else:
        print("La carga introducida no es correcta")
        exit()


def getResolucionInit():

    print("Introduzca la resolucion en pulgadas")
    resolucionInit = input()

    if resolucionInit.isnumeric() and int(resolucionInit) > 0:
        return resolucionInit
    else:
        print("La resolucion introducida no es correcta")
        exit()


def getFourKInit():

    print("Introduzca si es 4K")
    fourkInit = input()

    if fourkInit in ["True, true, TRUE, False, false, FALSE"]:
        return fourkInit
    else:
        print("Valor introducido no valido")

ejecutarScript()