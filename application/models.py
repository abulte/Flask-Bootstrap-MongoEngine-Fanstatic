#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Copyright 2013 Alexandre Bulté <alexandre[at]bulte[dot]net>
# 
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from mongoengine.queryset import DoesNotExist
from application import db, login_manager

class DummyContent(db.Document):
    title = db.StringField(required=True, max_length=50)
    description = db.StringField()
    active = db.BooleanField()

    def __unicode__(self):
        return self.title

# Create user model. For simplicity, it will store passwords in plain text.
# Obviously that's not right thing to do in real world application.
class User(db.Document):
    email = db.EmailField(max_length=120, primary_key=True)
    password = db.StringField(max_length=64)

    # Flask-Login integration
    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return self.email

    @classmethod
    def by_email(cls, email):
        try:
            return User.objects.get(email=email)
        except DoesNotExist:
            return None

    def __unicode__(self):
        return self.email

@login_manager.user_loader
def load_user(userid):
    return User.by_email(userid)
