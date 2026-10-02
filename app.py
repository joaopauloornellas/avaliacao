from flask import Flask, render_template, request

app = Flask(__name__)

app.secret_key = 'prova'

@app.route('/', methods=['GET', 'POST'])
def formulario():

    if request.method == 'POST':

        nome = request.form['nome']
        peso_str = request.form['peso']
        altura_str = request.form['altura']

        peso = int(peso_str)
        altura = float(altura_str)



        print(f'Dados recebidos: {nome} | {peso} | {altura}')

        imc = peso / (altura * altura)

        print(f'IMC = {imc}')

    return render_template('index.html', imc=imc, nome=nome)



@app.route('/equipe')
def equipe():

    return render_template('equipe.html')







if __name__ == '__main__':
    app.run(debug=True)
