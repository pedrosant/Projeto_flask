from pprint import pp
import string
from urllib.request import Request
from flask import Flask, request, render_template, redirect, url_for
from templates.controller.rotas import verif_rota
app = Flask(__name__)


@app.route('/logado', methods = ['POST','GET'])
def logado():
    rota = verif_rota('logado')               
    return render_template(rota)
    
@app.route('/usuario')
def Usuario():
    rota = verif_rota('usuario')
    return render_template(rota)

@app.route('/passageiro')
def Passageiro():
    rota = verif_rota('passageiro')
    return render_template(rota)

@app.route('/motorista')
def Motorista():
    rota = verif_rota('motorista')
    return render_template(rota)

@app.route('/veiculos')
def Veiculos():
    rota = verif_rota('veiculos')
    return render_template(rota)


@app.route("/", methods = ['POST','GET'])
def index():
    if request.method == 'POST':
        nome = request.form['login']
        senha = request.form['senha']
        if nome == 'seuze' and senha == '123':
            rota = verif_rota('logado')
            return render_template(rota) 
        else:
            return "Login ou senha incorreta"
    else:
        rota = verif_rota('/')
        return render_template(rota)    

if (__name__ == "__main__"):
    app.run(debug = True)


