#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Copyright 2013 Alexandre Bulté <alexandre[at]bulte[dot]net>
# 
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os

class GenericConfig(object):
    MONGODB_SETTINGS = {
        'DB': 'flask_db',
        'USERNAME': None,
        'PASSWORD': None,
        'HOST': 'localhost',
        'PORT': 27017
    }
    SECRET_KEY = 'thisissecretormaybenothatmuch'
    ADMIN_USER = 'admin@admin.com'
    ADMIN_PASSWORD = 'secret'

class ProductionConfig(GenericConfig):
    DEBUG = False
    FANSTATIC_OPTIONS = {
        'bottom': True, 
        'minified': True
    }

class DevelopmentConfig(GenericConfig):
    DEBUG = True
    FANSTATIC_OPTIONS = {
        'bottom': True, 
    }

def get_config():
    if os.environ.get('FLASK_ENV', '') == 'PROD':
        return 'application.settings.ProductionConfig'
    else:
        return 'application.settings.DevelopmentConfig'