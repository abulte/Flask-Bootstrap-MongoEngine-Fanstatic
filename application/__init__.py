#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Copyright 2013 Alexandre Bulté <alexandre[at]bulte[dot]net>
# 
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from flask import Flask, render_template, \
    redirect, request, url_for, flash
from flask_fanstatic import Fanstatic
from flask.ext.mongoengine import MongoEngine
from flask.ext.mongoengine.wtf import model_form
from flask.ext.superadmin import Admin

##- Init and configure -##

DEBUG = True
FANSTATIC_OPTIONS = {
    'bottom': True, 
    'minified': True
}
MONGODB_SETTINGS = {
    'DB': 'flask_db',
    'USERNAME': None,
    'PASSWORD': None,
    'HOST': 'localhost',
    'PORT': 27017
}
SECRET_KEY = 'thisissecretormaybenothatmuch'

app = Flask(__name__)
app.config.from_object(__name__)
fanstatic = Fanstatic(app)
db = MongoEngine(app)

# define your own ressources this way
fanstatic.resource('js/app.js', name='app_js', bottom=True)

##- Models -##

class DummyContent(db.Document):
    title = db.StringField(required=True, max_length=50)
    description = db.StringField()
    active = db.BooleanField()

    def __unicode__(self):
        return self.title

##- Views -##

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST', 'GET'])
def add():
    DummyContentForm = model_form(DummyContent)
    form = DummyContentForm()
    if request.method == 'POST' and form.validate():
        app.logger.debug('Validation passed...')
        content = DummyContent()
        form.populate_obj(content)
        content.save()
        flash('DummyContent saved.')
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

##- Admin -##

admin = Admin(app)
admin.register(DummyContent)