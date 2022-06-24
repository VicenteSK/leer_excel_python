from flask import Flask, render_template, request , jsonify
import pandas as pd

from validaciones import *

app = Flask(__name__)

@app.route('/data', methods =['GET', 'POST'])
def data():
    if request.method == 'GET':
        return render_template("index.html")

    if request.method == 'POST':
        file = request.files['archivo']
        print(file)
             
        if esExcel(file.filename):
            data = pd.read_excel(file) #convierte excel en dataframe
            if not estaVacio(data):
                if checkColumnas(data):
                    if checkDatosColumnas(data):
                        return data.to_json(orient="records"),200
                    else:
                        return "las columnas contienen errores", 400    
                else:
                    return "Error, no contiene todas las columnas", 400 
            else:
                return "Error, archivo excel vacio" , 400                
        else:
            if file.filename=="":
                return "Error no has cargado archivo" , 400 
            else:
                return "formato incorrecto, no es excel"  , 400   
             

if __name__ == '__main__':
    app.run(debug= True)
