import pprint

class Serie():

    titulo = ""
    n_temporadas = 3
    entregado = False
    genero = ""
    creador = ""

    def __init__(self, titulo, n_temporadas, entregado, genero, creador):
        self.titulo = titulo
        self.n_temporadas = n_temporadas
        self.entregado = entregado
        self.genero = genero
        self.creador = creador
        self.retornarArray()

    def retornarArray(self):

        arrayFinal = [self.titulo, self.n_temporadas, self.entregado, self.genero, self.creador]

        return arrayFinal


class Videojuego():
    titulo = ""
    horas_estimadas = 10
    entregado = False
    genero = ""
    compania = ""

    def __init__(self, titulo, horas_estimadas, entregado, genero, compania):
        self.titulo = titulo
        self.horas_estimadas = horas_estimadas
        self.entregado = entregado
        self.genero = genero
        self.compania = compania
        self.retornarArray()

    def retornarArray(self):

        arrayFinal = [self.titulo, self.horas_estimadas, self.entregado, self.genero, self.compania]

        return arrayFinal

def ejecutarScript():

    arrayGames = [
        Videojuego("Dark Souls", 35, False, "Rol", "From Software").retornarArray(),
        Videojuego("FIFA", 10, True, "Deportes", "EA").retornarArray(),
        Videojuego("Call Of Duty", 10, False, "Shooter", "Activision").retornarArray(),
        Videojuego("OverWatch", 10, True, "Shooter", "Activision").retornarArray(),
        Videojuego("DOOM", 10, True, "Shooter", "Bethesda").retornarArray()
    ]
    arraySeries = [
        Serie("Breaking Bad", 5, True, "Thriller", "Vince Gilligan").retornarArray(),
        Serie("La casa de papel", 5, False, "Accion", "Alex Pina").retornarArray(),
        Serie("Peaky Blinders", 6, True, "Thriller", "Steven Knight").retornarArray(),
        Serie("Narcos", 3, False, "Accion", "Chris Brancato").retornarArray(),
        Serie("Squid Game", 1, False, "Thriller", "Hwang Dong-hyuk").retornarArray()
    ]

    print("Indique cuantos/as videojuegos/series desea entregar")
    nObjetosEntregados = input()

    if nObjetosEntregados.isnumeric() and int(nObjetosEntregados) > 0:

        for i in range(int(nObjetosEntregados)):

            print("¿Que categoria desea entregar?")
            nameCategory = input()

            if nameCategory in ["Serie", "Series", "serie", "series", "SERIE", "SERIES"]:
                pprint.pprint(arraySeries)
                entregar(arraySeries)
            elif nameCategory in ["Videojuego", "videojuego", "VIDEOJUEGO", "videojuegos", "VIDEOJUEGOS", "Videojuegos"]:
                pprint.pprint(arrayGames)
                entregar(arrayGames)
            elif nameCategory in ["nada", "NADA", "N/A", "Nada"]:
                pprint.pprint(arraySeries)
                pprint.pprint(arrayGames)
                pintarArrays(arrayGames, arraySeries)

    else:
        print("El valor introducido no es valido")
        exit()

    pintarArrays(arrayGames, arraySeries)
    indicarMaximo(arrayGames, arraySeries)


def entregar(array):

    print("Indique el titulo que quiere entregar")
    nameTitle = input()

    for i in range(5):
        if array[i][0] == nameTitle:
            array[i][2] = True
            print(array[i][0] + " ha sido entregado")


def pintarArrays(arrayG, arrayS):

    arrayEntregados = []

    for i in range(5):
        if arrayG[i][2]:
            arrayEntregados.append(arrayG[i][0])
        if arrayS[i][2]:
            arrayEntregados.append(arrayS[i][0])

    lenEntregados = len(arrayEntregados)

    print("En total hay " + str(lenEntregados) + " entregados:")
    pprint.pprint(arrayEntregados)


def indicarMaximo(arrayG, arrayS):

    i = 1

    maxGamesHours = arrayG[i-1]
    maxSeriesSeasons = arrayS[i-1]

    for i in range(5):
        if(maxGamesHours[1] < arrayG[i][1]):
            maxGamesHours = arrayG[i]

        if(maxSeriesSeasons[1] < arrayS[i][1]):
            maxSeriesSeasons = arrayS[i]

    print("El videojuego con mas horas estimadas es " + str(maxGamesHours[0]))

    print("La serie con mas temporadas es " + str(maxSeriesSeasons[0]))

ejecutarScript()