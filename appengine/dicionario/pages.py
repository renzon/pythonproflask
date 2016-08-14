# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import dicionario
from dicionario.modelo import Verbete
from flask import render_template

verbete = dicionario.verbete


@verbete.route('/')
def listar():
    """Liste Verbetes"""
    query = Verbete.query().order(-Verbete.palavra).order(Verbete.criacao)
    verbetes = query.fetch()

    return render_template('listar.html',verbetes=verbetes)


@verbete.route('/salvar')
def salvar():
    """Salva um verbete em BD"""
    palavra = request.args['palavra']
    descricao = request.args.get('descricao')
    verbete = Verbete(palavra=palavra, descricao=descricao)
    verbete.put()
    return jsonify(verbete_dct(verbete))


@verbete.route('/editar/<int:id>')
def editar(id):
    """Salva um verbete em BD"""
    palavra = request.args['palavra']
    descricao = request.args.get('descricao')
    verbete = Verbete.get_by_id(id)
    verbete.palavra = palavra
    verbete.descricao = descricao
    verbete.put()
    return jsonify(verbete_dct(verbete))


@verbete.route('/apagar/<int:id>')
def apagar(id):
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