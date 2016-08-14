# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

"""
`appengine_config.py` is automatically loaded when Google App Engine
starts a new instance of your application. This runs before any
WSGI applications specified in app.yaml are loaded.
"""

from google.appengine.ext import vendor

# Third-party libraries are stored in "lib", vendoring will make
# sure that they are importable by the application.
vendor.add('lib')

from main import app  # this code must be here because depends on flask inside lib

print('App cfg')

from dicionario import verbete

app.register_blueprint(verbete, url_prefix='/verbetes')
print(app.url_map)
