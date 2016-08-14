# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from flask import Blueprint

verbete = Blueprint('verbete', __name__,template_folder='templates')

import dicionario.rest
import dicionario.pages
# print(rest)
