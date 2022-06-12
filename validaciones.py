def estaVacio(df):
    if (df.empty):
        print("esta vacio")
        return True
    else:
        print("no esta vacio")
        return False

def esExcel(file):
    if ".xls" in file:
        print("si es archivo excel")
        return True
    else:
        print("no es archivo excel")
        return False
        


def checkColumnas(df):
    columnas = ["Nombre", "ApellidoPaterno", "ApellidoMaterno", "Sexo", "Edad", "Run", "Parentesco"]
    for columna in columnas:
        if columna in df:
            print("si está esta columna " + columna)
        else:
            print("no se encuentra columna " + columna)
            return False
    return True
