from pprint import pp
import string
from urllib.request import Request
from flask import Flask, request, render_template, redirect, url_for
from rotas import verif_rota
app = Flask(__name__)


@app.route('/logado', methods = ['POST','GET'])
def logado():
    rota = verif_rota('logado') 
    print(rota)              
    return render_template(rota)
    
@app.route('/usuario')
def Usuario():
    return render_template('usuario.html')

@app.route('/passageiro')
def Passageiro():
    return render_template('passageiro.html')

@app.route('/motorista')
def Motorista():
    return render_template('motorista.html')

@app.route('/veiculos')
def Veiculos():
    return render_template('veiculos.html')


@app.route("/", methods = ['POST','GET'])
def index():
    if request.method == 'POST':
        usuario = request.form['id_user']
        password = request.form['id_password'] 
        print(usuario)
        return redirect(url_for('logado'))         
    return render_template('index.html')    

if (__name__ == "__main__"):
    app.run(debug = True)


