# -*- coding: utf-8 -*-
"""`main` is the top level module for your Flask application."""
from __future__ import absolute_import, unicode_literals

# Import the Flask Framework

from google.appengine.ext import ndb

from dicionario.modelo import Verbete
from flask import request, jsonify
from flask.json import jsonify

import dicionario

verbete = dicionario.verbete


@verbete.route('/api')
def listar_api():
    """Liste Verbetes"""
    query = Verbete.query().order(-Verbete.palavra).order(Verbete.criacao)
    verbetes = query.fetch()
    verbetes_dcts = [verbete_dct(v) for v in verbetes]
    return jsonify(verbetes_dcts)


@verbete.route('/api/salvar')
def salvar_api():
    """Salva um verbete em BD"""
    palavra = request.args['palavra']
    descricao = request.args.get('descricao')
    verbete = Verbete(palavra=palavra, descricao=descricao)
    verbete.put()
    return jsonify(verbete_dct(verbete))


@verbete.route('/api/editar/<int:id>')
def editar_api(id):
    """Salva um verbete em BD"""
    palavra = request.args['palavra']
    descricao = request.args.get('descricao')
    verbete = Verbete.get_by_id(id)
    verbete.palavra = palavra
    verbete.descricao = descricao
    verbete.put()
    return jsonify(verbete_dct(verbete))


@verbete.route('/api/apagar/<int:id>')
def apagar_api(id):
    """Salva um verbete em BD"""
    key = ndb.Key(Verbete, id)
    key.delete()
    return jsonify('ok')


def verbete_dct(verbete):
    dct = {
        'id': verbete.key.id(),
        'palavra': verbete.palavra,
        'descricao': verbete.descricao,
        'criacao': verbete.criacao,
        'update': verbete.update,
    }

    return dct
