# Sistema Web de Cadastro de Alunos

> Descrição da Atividade

## Objetivo
Desenvolver uma aplicação web utilizando Python, Flask, HTML e Pandas que permita o cadastro de alunos através de um formulário web, armazenando os dados em um arquivo CSV.

## Equipe 

> Grupo 3

- Rebeca Andrade Bivar
- Jorge Alexandre Araújo
- Eudes Rego Sousa Silva
- Paulo Henrique Bezerra da Silva
- Evelyn Karinne Macedo Mota Silva
- Diego de Souza Pinto
  
---

## Requisitos do Projeto

### 1. Programação Orientada a Objetos
Criar uma classe chamada `Pessoa` contendo os seguintes atributos:
* Nome
* Idade
* Telefone
* Endereço
* Hobby

**Implementar:**
* Método construtor (`__init__`)
* Métodos GET e SET para todos os atributos
* Criar um objeto chamado `aluno` que será instanciado a partir da classe `Pessoa`.

### 2. Interface Web
Desenvolver uma página HTML contendo um formulário para cadastro de alunos.

**Campos obrigatórios:**

| Campo | Tipo |
| :--- | :--- |
| Nome | Texto |
| Idade | Número |
| Telefone | Texto |
| Endereço | Texto |
| Hobby | Texto |

**Botão:**
* Salvar

### 3. Manipulação de Dados
Utilizar a biblioteca Pandas para:
* Criar um DataFrame contendo os dados recebidos do formulário.
* Adicionar novos registros ao DataFrame.
* Salvar os dados em um arquivo CSV.

### 4. Persistência dos Dados
O sistema deve:
* Criar automaticamente o arquivo `dados.csv` caso não exista.
* Adicionar novos registros sem apagar os anteriores.
* Manter os dados persistidos após o encerramento da aplicação.

---

## Arquitetura do Projeto

```text
projeto_final/
│
├── app.py
│
├── data/
│   └── dados.csv
│
└── templates/
    └── index.html
```

## Fluxo de Funcionamento

Usuário
   ↓
Formulário HTML
   ↓
Flask recebe os dados
   ↓
Objeto Aluno é criado
   ↓
Pandas cria DataFrame
   ↓
Dados são gravados em CSV
   ↓
Mensagem de confirmação

## Exemplo de Saída

nome,idade,telefone,endereco,hobby
João,20,99999-9999,Manaus,Leitura
Maria,21,98888-8888,Manaus,Música
Carlos,19,97777-7777,Parintins,Futebol

## Critérios de Avaliação

| Critério | Pontos |
| :--- | :---: |
| Classe Pessoa criada corretamente | 2,0 |
| Uso de métodos GET e SET | 1,0 |
| Instanciação do objeto aluno | 1,0 |
| Formulário HTML funcional | 2,0 |
| Utilização do Flask | 2,0 |
| Utilização do Pandas | 1,0 |
| Geração correta do CSV | 1,0 |
| **Total** | **10,0** |
