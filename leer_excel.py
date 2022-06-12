from flask import Flask, request , jsonify
import pandas as pd

app = Flask(__name__)

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

@app.route('/data', methods =['GET', 'POST'])
def data():
    if request.method == 'GET':
        # file = request.form['upload-file']
        file1 = "integrantesfamiliareceptora.xlsx"
        file2 = "integrantesvacio.xlsx"
        file3 = "integrantes4columnas.xlsx"
        file4 = "integrantessinapellidomaterno.xlsx"
        file5 = "pruebaword.docx"
        file6 = "hola.xls.docx"

        esExcel(file6)
        data = pd.read_excel(file4)
        #convierte excel en dataframe

        # 1º validacion: que no este vacio

        estaVacio(data)
        
        checkColumnas(data)

       # VALIDACIONE 1 que llegue el archivo
        # VALIDACIONE 2.que sea Excel **1/2 
        # VALIDACIONE 3.que no venga vacio *ok*****
        # VALIDACIONE 4 que vengan todas las columnas (en este caso el ejemplo es 7) **OK
        # VALIDACIONE 15. que los datos de cada columna respeten el contrato (ejemplo nombre, que no tenga números, email, rut)
        ###
    
        #return "data"
        #if not file.endswith('.xls'):
           # return {'error': 'no es un archivo excel'}

         # // validacion de campos en tabla excel, en donde
         # toma los datos de las tablas, lo transforma a una lista porque esta hecho en python
          #para asi pasarlos a un .json//  
    #try: 
        #cursor=conexion.connection.cursor()
        #sql = "SELECT Nombre, ApellidoPaterno, ApellidoMaterno, Sexo, Edad, Run, Parentesco FROM integrantesfamiliareceptora"  
        
        
        return data.to_json()
    


if __name__ == '__main__':
    app.run(debug= True)
