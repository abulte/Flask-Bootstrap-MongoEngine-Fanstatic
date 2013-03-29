#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Copyright 2013 Alexandre Bulté <alexandre[at]bulte[dot]net>
# 
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from mongoengine.queryset import DoesNotExist
from flask import Flask, render_template, \
    redirect, request, url_for, flash
from flask_fanstatic import Fanstatic
from flask.ext import wtf
from flask.ext.mongoengine import MongoEngine
from flask.ext.mongoengine.wtf import model_form
from flask.ext.superadmin import Admin, AdminIndexView
from flask.ext.superadmin.model.backends.mongoengine import ModelAdmin
from flask.ext.login import LoginManager, login_user, login_required, \
    logout_user, current_user

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
ADMIN_USER = 'admin@admin.com'
ADMIN_PASSWORD = 'secret'

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

##- Forms -##

DummyContentForm = model_form(DummyContent)

class LoginForm(wtf.Form):
    email = wtf.TextField(validators=[wtf.required(), wtf.validators.Email()])
    password = wtf.PasswordField(validators=[wtf.required()])

##- Views -##

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST', 'GET'])
@login_required
def add():
    form = DummyContentForm()
    if request.method == 'POST' and form.validate():
        content = DummyContent()
        form.populate_obj(content)
        content.save()
        flash('DummyContent saved.')
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

##- Login -##

login_manager = LoginManager()
login_manager.setup_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(userid):
    return User.by_email(userid)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.by_email(form.email.data)
        if user is not None and user.password == form.password.data:
            login_user(user)
            flash("Logged in successfully.")
            return redirect(request.args.get("next") or url_for("index"))
        else:
            flash('Wrong credentials')
    return render_template("login.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('Logged out.')
    return redirect(url_for('index'))

##- Admin -##

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