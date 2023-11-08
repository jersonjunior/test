from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import pandas as pd
import time, sys, os, io, subprocess, urllib3, json, requests, pyodbc

urllib3.disable_warnings()

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
auth = HTTPBasicAuth()

users = {
    "ContraCheque": generate_password_hash("@#Limbos2023Sefaz@#")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route('/CitConnect', methods=['POST'])
@auth.login_required
