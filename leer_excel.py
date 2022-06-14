from flask import Flask, render_template, request , jsonify
import pandas as pd

from validaciones import *

app = Flask(__name__)

@app.route('/data', methods =['GET', 'POST'])
def data():
    if request.method == 'GET':
        return render_template("index.html")

    if request.method == 'POST':
        file = request.files['file']
        print(file)
             
        if esExcel(file.filename):
            data = pd.read_excel(file) #convierte excel en dataframe
            if not estaVacio(data):
                if checkColumnas(data):
                    if checkDatosColumnas(data):
                        return data.to_json()
                    else:
                        return "las columnas contienen errores"    
                else:
                    return "Error, no contiene todas las columnas"
            else:
                return "Error, archivo excel vacio"                
        else:
            if file.filename=="":
                return "Error no has cargado archivo" 
            else:
                return "formato incorrecto, no es excel"    
             

if __name__ == '__main__':
    app.run(debug= True)
