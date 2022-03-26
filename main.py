from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/logado')
def logado():    
    return render_template('home.html')


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


