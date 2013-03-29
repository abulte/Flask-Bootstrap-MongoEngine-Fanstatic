#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Copyright 2013 Alexandre Bulté <alexandre[at]bulte[dot]net>
# 
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from flask import Flask
from flask_fanstatic import Fanstatic
from flask.ext.mongoengine import MongoEngine
from flask.ext.login import LoginManager

from .settings import get_config

##- Init and configure -##

app = Flask(__name__)
app.config.from_object(get_config())
db = MongoEngine(app)

##- Login -##

login_manager = LoginManager()
login_manager.setup_app(app)
login_manager.login_view = "login"

##- Resources -##

fanstatic = Fanstatic(app)
fanstatic.resource('js/app.js', name='app_js', bottom=True)

##- Imports -##

import views
import admin
