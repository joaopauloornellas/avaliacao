from flask import Flask, render_template

app = Flask(__name__)

app.secretkey = 'prova'

@app.route('/')
def formulario():

    return render_template('index.html')






@app.route('/equipe')
def equipe():

    return render_template('equipe.html')







if __name__ == '__main__':
    app.run(debug=True)
