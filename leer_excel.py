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

def esExcel(df):
    #... algo que valide que sea un excel

def checkColumnas(df):
    #..



@app.route('/data', methods =['GET', 'POST'])
def data():
    if request.method == 'GET':
        # file = request.form['upload-file']
        file = "integrantesfamiliareceptora.xlsx"
        # file = "integrantesvacio.xlsx"
        data = pd.read_excel(file)

        # 1º validacion: que no este vacio
        estaVacio(data)

       # VALIDACIONE 1 que llegue el archivo
        # VALIDACIONE 2.que sea Excel
        # VALIDACIONE 3.que no venga vacio ******
        # VALIDACIONE 4 que vengan todas las columnas (en este caso el ejemplo es 7)
        # VALIDACIONE 15. que los datos de cada columna respeten el contrato (ejemplo nombre, que no tenga números, email, rut)
        ###
    
        return "data"
        #if not file.endswith('.xls'):
           # return {'error': 'no es un archivo excel'}

         # // validacion de campos en tabla excel, en donde
         # toma los datos de las tablas, lo transforma a una lista porque esta hecho en python
          #para asi pasarlos a un .json//  
    #try: 
        #cursor=conexion.connection.cursor()
        #sql = "SELECT Nombre, ApellidoPaterno, ApellidoMaterno, Sexo, Edad, Run, Parentesco FROM integrantesfamiliareceptora"  
        
        
        # return data.to_json()
    


if __name__ == '__main__':
    app.run(debug= True)
