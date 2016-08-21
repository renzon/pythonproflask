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
        key_id = v.key.id()
        v.delete_path = url_for('verbete.apagar', id=key_id)
        v.edit_path = url_for('verbete.form', id=key_id)
    return render_template(
        'listar.html',
        verbetes=verbetes,
        novo_url=url_for('verbete.form')
    )


@verbete.route('/editar/<int:id>', methods=['POST'])
def editar(id):
    """Edita um verbete em BD"""
    palavra = request.form.get('palavra')
    descricao = request.form.get('descricao')
    verbete = Verbete.get_by_id(id)
    verbete.populate(palavra=palavra, descricao=descricao)
    verbete.put()
    return redirect(url_for('verbete.listar'))


@verbete.route('/form/<int:id>')
@verbete.route('/form', defaults={'id': None})
def form(id):
    """Mostra form de verbete"""
    verbete = None if id is None else Verbete.get_by_id(id)
    form_url = url_for('verbete.save') if id is None else url_for('verbete.editar', id=id)
    return render_template('form.html', verbete=verbete, form_url=form_url)


@verbete.route('/salvar', methods=['POST'])
def save():
    """Liste Verbetes"""
    palavra = request.form.get('palavra')
    descricao = request.form.get('descricao')
    verbete = Verbete(palavra=palavra, descricao=descricao)
    verbete.put()
    return redirect(url_for('verbete.listar'))


@verbete.route('/apagar/<int:id>', methods=['POST'])
def apagar(id):
    """Salva um verbete em BD"""
    key = ndb.Key(Verbete, id)
    key.delete()
    return redirect(url_for('verbete.listar'))
