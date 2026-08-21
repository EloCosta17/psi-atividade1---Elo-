from flask import Flask, render_template,
import models

app = Flask(__name__)
app.secret_key = 'chavesecreta'
usuario = models.usuarios()

@app.route('/')
def inicio():
    if "usuario" in session:
        return f'{session["usuario"] logado}'
    return render_template('index.html')

@app.route('/login' methods=['POST','GET'])
def login():
    if request.method == 'POST':
        session['usuario'] = usuario
        return redirect(url_for('listagem'))

@app.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/listagem')
def listagem():



if __name__ == 'main':
    app.run(debug=True)