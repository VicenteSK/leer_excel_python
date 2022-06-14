from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype

def estaVacio(df):
    if (df.empty):
        print("esta vacio")
        return True
    else:
        print("no esta vacio")
        return False

def esExcel(file):
    extension = file.split(".")[-1]
    print("extension es " + extension)
    if "xls" in extension:
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

def checkDatosColumnas(df):
    print(df.dtypes)
    if is_string_dtype(df['Nombre']) and is_string_dtype(df['ApellidoPaterno'])and is_string_dtype(df['ApellidoMaterno']) and is_string_dtype(df['Sexo']) and is_string_dtype(df['Run']) and is_string_dtype(df['Parentesco'])and is_numeric_dtype(df['Edad']):
        return True
    else:
        return False    
