from flask import jsonify, Blueprint, request, abort, render_template, flash, url_for, redirect

ap1_blueprint = Blueprint('ap1', 'ap1', url_prefix='/ap1')

numero = 0

@ap1_blueprint.route('/', methods=['GET', 'POST'])
def tarefa():
    if request.method == 'POST':
        numero = request.form['number']
        numero = int(numero)
        if not numero and numero != 0:
            flash('Insira um número para enviar')
        else:
            numero = (10*numero)+8
            return render_template('tarefa.html', numero=numero)
    return render_template('tarefa.html')
