import os
from flask import Flask, render_template, request, flash, redirect, url_for
import pandas as pd

# importando a classe Pessoa do arquivo pessoa.py
from pessoa import Pessoa

app = Flask(__name__)
app.secret_key = 'my_super_cool_secret_key' # heheh :)

# path config
DATA_DIR = 'data'
CSV_PATH = os.path.join(DATA_DIR, 'dados.csv')

# --- persistência dos dados ---
os.makedirs(DATA_DIR, exist_ok=True)

# form
@app.route('/')
def index():
    return render_template('index.html')


# rota de processamento
@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    if request.method == 'POST':
        # flask recebendo os dados do formulário HTML
        nome = request.form.get('nome')
        idade = request.form.get('idade')
        telefone = request.form.get('telefone')
        endereco = request.form.get('endereco')
        hobby = request.form.get('hobby')

        # objeto aluno é instanciado a partir da classe pessoa
        aluno = Pessoa(nome, idade, telefone, endereco, hobby)

        # criando o dicionário acessando os dados com os métodos GET
        dados_novos = {
            'nome': [aluno.get_nome()],
            'idade': [aluno.get_idade()],
            'telefone': [aluno.get_telefone()],
            'endereco': [aluno.get_endereco()],
            'hobby': [aluno.get_hobbies()]
        }
        
        # pandas dataframe
        df_novo = pd.DataFrame(dados_novos)

        # vendo se o o arquivo já existe para decidir se inclui o cabeçalho
        arquivo_existe = os.path.exists(CSV_PATH)
        
        # sdiciona os dados ao CSV sem apagar os anteriores 
        df_novo.to_csv(CSV_PATH, 
                       mode='a', 
                       index=False, 
                       header=not arquivo_existe, 
                       encoding='utf-8') # utf-8, estou no linux

        flash(f"Aluno {aluno.get_nome()} cadastrado com sucesso!", "success")
        
        return redirect(url_for('index'))


if __name__ == '__main__':
    # local server
    app.run(debug=True)