# -*- coding: utf-8 -*-
"""`main` is the top level module for your Flask application."""
from __future__ import absolute_import, unicode_literals

# Import the Flask Framework
from dicionario.modelo import Verbete
from flask import Flask, request

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
    key = verbete.key
    return 'Verbete salvo com key kind {} id {}'.format(key.kind(), key.id())


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
