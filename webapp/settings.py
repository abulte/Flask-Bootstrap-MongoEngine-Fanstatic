#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Copyright 2013 Alexandre Bulté <alexandre[at]bulte[dot]net>
# 
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os
import json

from webapp import app

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

class DotcloudConfig(ProductionConfig):

    DEBUG = True

    dotcloud_env = {}
    try:
        dotcloud_env_file_path = os.path.expanduser('~/environment.json')
        with open(dotcloud_env_file_path) as f:
            dotcloud_env.update(json.load(f))
    except Exception as e:
        app.logger.error('unable to load file : %s, exception : %s' % (format(dotcloud_env_file_path), e))

    # You should not use "/admin" user for production env.
    MONGODB_SETTINGS = dict(host=dotcloud_env.get('DOTCLOUD_DATA_MONGODB_URL','novalue') + '/admin', db='flask_db')

class DevelopmentConfig(GenericConfig):
    DEBUG = True
    FANSTATIC_OPTIONS = {
        'bottom': True, 
    }
