#!/bin/python3.8

from flask import Flask, request
import pymysql, os, subprocess, sys, time, sqlalchemy, urllib3, urllib.parse, json, requests, pandas as pd
from sqlalchemy import MetaData
from multiprocessing import Process
from threading import Thread
urllib3.disable_warnings()

app = Flask(__name__)

ack = None
messages = None

## Credenciais do usuario citsmart para os modulos
User = 'cit.local\cissa.admin'
Pass = '!@p3@j@4dAwb'

## mensagem Hello Word
@app.route("/noc", methods=['POST'])
def noc():
    response = request.get_json()
    print(response['Nome'])
    return "Hello, World!"


######################################
# Rota do aplicativo vindo do Citsmart
@app.route("/resetsenha", methods=['POST', 'GET'])
def resetsenha():
    response = request.get_json()
    print(response)
    # variaveis vindas do Citsmart
    ticket = response['ticket']
    nome = response['nome']
    email = response['email']
    print(f'O nome é {nome} O email é {email}')

    print('Inicio do processo')
    background_thread = Thread(target=check_process_resetsenha, args=(ticket,nome,email))
    background_thread.start()
    return "Tudo OK!"
# Executar o Modulo
def check_process_resetsenha(ticket,nome, email):
    exec(open("/opt/automacao/modulos/resetsenha.py").read())
    print('conclusao do processo')

######################################
# Rota do aplicativo vindo do Citsmart
@app.route("/AtualizarDadosUsuarioADAuto", methods=['POST', 'GET'])
def AtualizarDadosUsuarioADAuto():
    response = request.get_json()
    # variaveis vindas do Citsmart
    ticket = response['ticket']
    username = (response['username'])
    username = username.split('\\')[1]
    telefonefixo = response['telefonefixo']
    cep = response['cep']
    enderecoresidencial = response['enderecoresidencial']
    emailalternativo = response['emailalternativo']
    telefonemovel = response['telefonemovel']

    background_thread = Thread(target=check_process_AtualizarDadosUsuarioADAuto, args=(ticket,username,telefonefixo,cep,enderecoresidencial,emailalternativo,telefonemovel))
    background_thread.start()
    return "Tudo OK!"
# Executar o Modulo
def check_process_AtualizarDadosUsuarioADAuto(ticket,username,telefonefixo,cep,enderecoresidencial,emailalternativo,telefonemovel):
    exec(open("/opt/automacao/modulos/AtualizarDadosUsuarioADAuto.py").read())
######################################

@app.route("/CriarFtp", methods=['POST', 'GET'])
def CriarFtp():
    response = request.get_json()
    ## Caso desejar efetuar um print nas variaveis vindas do Citsmart
    #print(response['VAR'])
    ## Declaracao das varivaveis vindas do Citsmart 
    Diretorio = response['Diretorio']
    Ticket = response['Ticket']
    background_thread = Thread(target=check_process_CriarFtp, args=(Diretorio, Ticket))
    background_thread.start()
    return "Tudo OK!"
# Executar o Modulo
def check_process_CriarFtp(Diretorio, Ticket):
    exec(open("/opt/automacao/modulos/criar-ftp.py").read())
######################################
@app.route("/RmFtp", methods=['POST', 'GET'])
def RmFtp():
    response = request.get_json()
    ## Declaracao das varivaveis vindas do Citsmart
    Diretorio = response['Diretorio']
    Ticket = response['Ticket']
    background_thread = Thread(target=check_process_RmFtp, args=(Diretorio, Ticket))
    background_thread.start()
    return "Tudo OK!"
def check_process_RmFtp(Diretorio, Ticket):
    exec(open("/opt/automacao/modulos/rm-ftp.py").read())
######################################
@app.route("/AlterarPermissaoFtp", methods=['POST', 'GET'])
def AlterarPermissaoFtp():
    response = request.get_json()
    #print(response)
    ticket = response['Ticket']
    usuario = response['Usuario']
    repositorio = response['Repositorio']
    background_thread = Thread(target=check_process_AlterarPermissaoFtp, args=(ticket, usuario, repositorio))
    background_thread.start()
    return "Conexao com Citsmart OK!"
def check_process_AlterarPermissaoFtp(ticket, usuario, repositorio):
    exec(open("/opt/automacao/modulos/alterar-permissao-ftp.py").read())
######################################
@app.route("/AcessoWifi", methods=['POST', 'GET'])
def AcessoWifi():
    response = request.get_json()
    ## Declaracao das varivaveis vindas do Citsmart
    print(response)
    Ticket = response['Ticket']
    Nome = response['Nome']
    Cargo = response['Cargo']
    background_thread = Thread(target=check_process_AcessoWifi, args=(Ticket, Nome, Cargo))
    background_thread.start()
    return "Coleta do Citsmart OK!"
def check_process_AcessoWifi(Nome, Cargo, Ticket):
    exec(open("/opt/automacao/modulos/acesso-wifi.py").read())
######################################
@app.route("/AcessoBd", methods=['POST', 'GET'])
def AcessoBd():
    response = request.get_json()
    ticket = response['Ticket']
    login = response['Login']
    tipo = response['Tipo']
    background_thread = Thread(target=check_process_AcessoBd, args=(ticket, login, tipo))
    background_thread.start()
    return "Conexao com Citsmart OK!"
def check_process_AcessoBd(ticket, login, tipo):
    exec(open("/opt/automacao/modulos/acesso-bd.py").read())
######################################
@app.route("/AcessoBdAlt", methods=['POST', 'GET'])
def AcessoBdAlt():
    response = request.get_json()
    ticket = response['Ticket']
    login = response['Login']
    tipo = response['Tipo']
    background_thread = Thread(target=check_process_AcessoBdAlt, args=(ticket, login, tipo))
    background_thread.start()
    return "Coleta do Citsmart OK!"
def check_process_AcessoBdAlt(ticket, login, tipo):
    exec(open("/opt/automacao/modulos/acesso-bd-alt.py").read())
######################################
@app.route("/AcessoBdRm", methods=['POST', 'GET'])
def AcessoBdRm():
    response = request.get_json()
    print(response)
    ticket = response['Ticket']
    login = response['Login']
    tipo = response['Tipo']
    background_thread = Thread(target=check_process_AcessoBdRm, args=(ticket, login, tipo))
    background_thread.start()
    return "Conexao com Citsmart OK!"
def check_process_AcessoBdRm(ticket, login, tipo):
    exec(open("/opt/automacao/modulos/acesso-bd-rm.py").read())
######################################
@app.route("/AdDesbloqueiaUser", methods=['POST', 'GET'])
def adDesbloqueiaUser():
    response = request.get_json()
    print(response)
    comando = response['Comando']
    comando1 = 'ssh'
    ticket = response['Ticket']
    background_thread = Thread(target=check_process_AdDesbloqueiaUser, args=(comando, comando1, ticket))
    background_thread.start()
    return "Conexao com Citsmart OK!"
def check_process_AdDesbloqueiaUser(comando, comando1, ticket):
    exec(open("/opt/automacao/modulos/ad-desbloqueia-user.py").read())
######################################
@app.route("/AdDisableUser", methods=['POST', 'GET'])
def adDisableUser():
    response = request.get_json()
    #print(response)
    comando = response['Comando']
    comando1 = 'ssh'
    ticket = response['Ticket']
    background_thread = Thread(target=check_process_AdDisableUser, args=(comando, comando1, ticket))
    background_thread.start()
    return "Conexao com Citsmart OK!"
def check_process_AdDisableUser(comando, comando1, ticket):
    exec(open("/opt/automacao/modulos/ad-disable-user.py").read())
######################################
@app.route("/AlterarPermissaoCompartilhamento", methods=['POST', 'GET'])
def AlterarPermissaoCompartilhamento():
    response = request.get_json()
    print(response)
    ticket = response['Ticket']
    usuario = response['usuario']
    compartilhamento = response['compartilhamento']
    niveldeacesso = response['niveldeacesso']
    background_thread = Thread(target=check_process_AlterarPermissaoCompartilhamento, args=(ticket, usuario, compartilhamento, niveldeacesso))
    background_thread.start()
    return "Conexao com Citsmart OK!"
def check_process_AlterarPermissaoCompartilhamento(ticket, usuario, compartilhamento, niveldeacesso):
    exec(open("/opt/automacao/modulos/alterar-permissao-compartilhamento.py").read())
######################################
@app.route("/InstalarSoftware", methods=['POST', 'GET'])
def InstalarSoftware():
    response = request.get_json()
    print(response)
    ticket = response['Ticket']
    patrimonio = response['patrimonio']
    software = response['software']
    background_thread = Thread(target=check_process_InstalarSoftware, args=(ticket, patrimonio, software))
    background_thread.start()
    return "Conexao com Citsmart OK!"
def check_process_InstalarSoftware(ticket, patrimonio, software):
    exec(open("/opt/automacao/modulos/instalar-software.py").read())
######################################
@app.route("/AdCriarVmHyperV", methods=['POST', 'GET'])
def adCriarVmHyperVr():
    response = request.get_json()
    print(response)
    #print(response['OS'])
    #print(response['Template'])
    #print(response['Ticket'])
    #print(response['Ambiente'])
    os = response['OS']
    comando1 = 'ssh'
    comando = 'vai'
    ticket = response['Ticket']
    template = response['Template']
    ambiente = response['AmbienteVM']
    background_thread = Thread(target=check_process_AdCriarVmHyperV, args=(os, template, ticket, ambiente))
    background_thread.start()
    return "Conexao com Citsmart OK"
def check_process_AdCriarVmHyperV(os, template, ticket, ambiente):
    print("Tudo OK")

# Execução do aplicativo
if __name__ == "__main__":
    from waitress import serve
    ## Modo producao
    #serve(app, host="0.0.0.0", port=5000)
    ## Modo debug
    app.run(host='0.0.0.0', port=5000, debug=True)
