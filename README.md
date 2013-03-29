# Flask Bootstrap MongoEngine Fanstatic

## Purpose

Bootstraps a simple [Flask](http://flask.pocoo.org) app with:

* [Twitter Bootstrap](http://twitter.github.com/bootstrap/) integration via [Fanstatic](http://www.fanstatic.org/en/latest/).
* [MongoEngine](http://mongoengine.org) and [WTForms](http://wtforms.simplecodes.com/docs/) via [Flask-MongoEngine](https://flask-mongoengine.readthedocs.org/en/latest/)
* Administration interface via [Flask-SuperAdmin](http://flask-superadmin.readthedocs.org/en/latest/)
* Authentification with [Flask-Login](http://flask-login.readthedocs.org/en/latest/)

## Usage

You need a running MongoDB server.

	# […] create and activate a virtualenv
	git clone https://github.com/abulte/Flask-Bootstrap-MongoEngine-Fanstatic.git
	cd Flask-Bootstrap-MongoEngine-Fanstatic
	pip install -r requirements.txt
    python manage.py create_admin_user
	python manage.py runserver

Go to <http://localhost:4000>. Default admin user/password is: admin@admin.com/secret.
	
## Features

* Admin interface at `/admin`
* WTForms example at `/add`
* Login and logout at `/login` and `/logout`

## TODO

* Blueprints?
