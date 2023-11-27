import os
import csv
from flask import Flask, request
from flask import render_template, url_for, redirect

app = Flask(__name__)


os.environ['FLASK_DEBUG'] = 'True'
app.debug = os.environ.get('FLASK_DEBUG') == 'True'



@app.route('/')
def index():
    

    
        return render_template(
        'index.html',
        )
    

@app.route('/novo_termo')
def novo_termo():
    return render_template('adicionar_termo.html')


@app.route('/criar_termo', methods=['POST', ])
def criar_termo():

    termo = request.form['termo']
    definicao = request.form['definicao']

    with open(
            'bd_glossario.csv.txt',
            'a',
            newline='',
            encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo, delimiter=';')
        escritor.writerow([termo, definicao])

        return redirect(url_for('index'))

@app.route('/excluir_termo/<int:termo_id>', methods=['POST', ])
def excluir_termo(termo_id):

    with open(
            'bd_glossario.csv.txt', 'r',
            newline='', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        linhas = list(leitor)

    for i, linha in enumerate(linhas):
        if i == termo_id:
            del linhas[i]
            break

    with open(
            'bd_glossario.csv.txt', 'w',
            newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(linhas)

        return redirect(url_for('index'))
    
@app.route("/glossario")
def listar_termo(): 
    
    glossario_de_termos = []

   
    with open(
            'bd_glossario.csv.txt',
            newline='',
            encoding='utf-8') as arquivo:

        leitor = csv.reader(arquivo, delimiter=';')

        for linha in leitor:
            glossario_de_termos.append(linha)

    
        return render_template(
        'glossario.html',
        glossario_de_termos=glossario_de_termos)
    

@app.route("/sobre")
def sobre():
        

    return render_template('sobre.html')

@app.route("/tarefa")
def listar_tarefa(): 
    
    tarefa_de_termos = []

   
    with open(
            'bd_tarefa.csv',
            newline='',
            encoding='utf-8') as arquivo:

        leitor = csv.reader(arquivo, delimiter=';')

        for linha in leitor:
            tarefa_de_termos.append(linha)

    
        return render_template(
        'tarefa.html',
        tarefa_de_termos=tarefa_de_termos)
    
@app.route('/novo_tarefa')
def novo_tarefa():
    return render_template('adicionar_tarefa.html')

@app.route('/criar_tarefa', methods=['POST', ])
def criar_tarefa():

    termo = request.form['tarefa']
    definicao = request.form['definicao2']

    with open(
            'bd_tarefa.csv',
            'a',
            newline='',
            encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo, delimiter=';')
        escritor.writerow([termo, definicao])

        return redirect(url_for('index'))
    
@app.route('/excluir_tarefa/<int:tarefa_id>', methods=['POST', ])
def excluir_tarefa(tarefa_id):

    with open(
            'bd_tarefa.csv', 'r',
            newline='', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        linhas = list(leitor)

    for i, linha in enumerate(linhas):
        if i == tarefa_id:
            del linhas[i]
            break

    with open(
            'bd_tarefa.csv', 'w',
            newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(linhas)

        return redirect(url_for('index'))

    


if __name__ == '__main__':
    app.run()