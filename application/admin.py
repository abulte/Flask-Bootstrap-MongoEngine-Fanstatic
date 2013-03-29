#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Copyright 2013 Alexandre Bulté <alexandre[at]bulte[dot]net>
# 
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from flask.ext.superadmin import Admin, AdminIndexView
from flask.ext.superadmin.model.backends.mongoengine import ModelAdmin
from flask.ext.login import current_user

from application import app
from .models import User, DummyContent

# Create customized model view class
class MyModelView(ModelAdmin):
    def is_accessible(self):
        return current_user.is_authenticated()


# Create customized index view class
class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated()

# Create admin
admin = Admin(app, 'Backoffice', index_view=MyAdminIndexView())

# Add view
admin.add_view(MyModelView(User))
admin.add_view(MyModelView(DummyContent))