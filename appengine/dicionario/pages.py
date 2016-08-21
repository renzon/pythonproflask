# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from google.appengine.ext import ndb

import dicionario
from dicionario.modelo import Verbete
from flask import render_template, url_for, request, redirect

verbete = dicionario.verbete


@verbete.route('/')
def listar():
    """Liste Verbetes"""
    query = Verbete.query().order(-Verbete.palavra).order(Verbete.criacao)
    verbetes = query.fetch()
    for v in verbetes:
        v.delete_path = url_for('verbete.apagar', id=v.key.id())

    return render_template('listar.html', verbetes=verbetes)


@verbete.route('/form')
def form():
    """Salva um verbete em BD"""
    # palavra = request.args['palavra']
    # descricao = request.args.get('descricao')
    # verbete = Verbete(palavra=palavra, descricao=descricao)
    # verbete.put()
    query = Verbete.query().order(-Verbete.palavra).order(Verbete.criacao)
    verbetes = query.fetch()

    return render_template('form.html', verbetes=verbetes)


@verbete.route('/salvar', methods=['POST'])
def save():
    """Liste Verbetes"""
    palavra = request.form.get('palavra')
    descricao = request.form.get('descricao')
    verbete = Verbete(palavra=palavra, descricao=descricao)
    verbete.put()
    return redirect(url_for('verbete.listar'))


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


@verbete.route('/apagar/<int:id>', methods=['POST'])
def apagar(id):
    """Salva um verbete em BD"""
    key = ndb.Key(Verbete, id)
    key.delete()
    return redirect(url_for('verbete.listar'))
