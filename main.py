from flask import Flask, make_response, render_template
from route.ap1 import ap1_blueprint

app = Flask("LinguagemScript")
app.config['SECRET_KEY'] = 'secret key'

@app.route('/', methods=['GET'])
def explica():
    return render_template('explica.html')

@app.route('/descricao', methods=['GET'])
def inicio():
    return render_template('inicial.html')

app.register_blueprint(ap1_blueprint)

if __name__ == "__main__":
    app.run(debug=True)