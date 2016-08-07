# -*- coding: utf-8 -*-
"""`main` is the top level module for your Flask application."""
from __future__ import absolute_import, unicode_literals

# Import the Flask Framework
from dicionario.modelo import Verbete
from flask import Flask, request, json, jsonify

app = Flask(__name__)


# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/verbete')
def listar():
    """Return a friendly HTTP greeting."""
    return 'Listando Verbetes'


@app.route('/verbete/salvar')
def salvar():
    """Salva um verbete em BD"""
    palavra = request.args['palavra']
    descricao = request.args.get('descricao')

    verbete = Verbete(palavra=palavra, descricao=descricao)
    verbete.put()
    return verbete_json(verbete)


def verbete_json(verbete):
    dct = {
        'id': verbete.key.id(),
        'palavra': verbete.palavra,
        'descricao': verbete.descricao,
        'criacao': verbete.criacao,
        'update': verbete.update,
    }

    return jsonify(dct  )
