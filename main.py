#!/usr/bin/env python
# coding: utf8
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KINs, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from __future__ import unicode_literals

import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world 2!')


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
