from flask import Flask, request 
import pandas as pd

app = Flask(__name__)

@app.route('/data', methods =['GET', 'POST'])
def data():
    if request.method == 'POST':
        file = request.form['upload-file']
        data = pd.read_excel(file)
        return data.to_json()


if __name__ == '__main__':
    app.run(debug= True)
