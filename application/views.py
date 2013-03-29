#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Copyright 2013 Alexandre Bulté <alexandre[at]bulte[dot]net>
# 
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from flask import render_template, \
    redirect, request, url_for, flash

from application import app
from .forms import DummyContentForm, LoginForm
from .models import DummyContent, User
from flask.ext.login import login_user, login_required, \
    logout_user

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
