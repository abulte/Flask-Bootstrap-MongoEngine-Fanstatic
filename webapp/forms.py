#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Copyright 2013 Alexandre Bulté <alexandre[at]bulte[dot]net>
# 
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from flask.ext import wtf
from flask.ext.mongoengine.wtf import model_form

from .models import DummyContent

DummyContentForm = model_form(DummyContent)

class LoginForm(wtf.Form):
    email = wtf.TextField(validators=[wtf.required(), wtf.validators.Email()])
    password = wtf.PasswordField(validators=[wtf.required()])
