from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def consultar_estoque():
    estoque = []
    return render_template('estoque.html', titulo='Estoque')



if __name__ == '__main__': 
    app.run(debug=True)