# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from google.appengine.ext import ndb

from gaeforms.ndb.form import ModelForm


class Verbete(ndb.Model):
    criacao = ndb.DateTimeProperty(auto_now_add=True)
    update = ndb.DateTimeProperty(auto_now=True)
    palavra = ndb.StringProperty(required=True)
    descricao = ndb.TextProperty(required=True)
    silabas = ndb.IntegerProperty(default=0)

class VerbeteForm(ModelForm):
    _model_class = Verbete
    _include = [Verbete.palavra, Verbete.descricao, Verbete.silabas]

