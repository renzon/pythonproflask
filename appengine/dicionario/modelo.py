# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from google.appengine.ext import ndb


class Verbete(ndb.Model):
    criacao=ndb.DateTimeProperty(auto_now_add=True)
    update = ndb.DateTimeProperty(auto_now=True)
    palavra = ndb.StringProperty(required=True)
    descricao = ndb.TextProperty(required=True)
