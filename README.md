# Flask Bootstrap MongoEngine Fanstatic

## Purpose

Bootstraps a simple [Flask](http://flask.pocoo.org) app with:

* [Twitter Bootstrap](http://twitter.github.com/bootstrap/) integration via [Fanstatic](http://www.fanstatic.org/en/latest/).
* [MongoEngine](http://mongoengine.org) and [WTForms](http://wtforms.simplecodes.com/docs/) via [Flask-MongoEngine](https://flask-mongoengine.readthedocs.org/en/latest/)
* Administration interface via [Flask-SuperAdmin](http://flask-superadmin.readthedocs.org/en/latest/)

## Usage

	# […] create and activate a virtualenv
	git clone https://github.com/abulte/Flask-Bootstrap-MongoEngine-Fanstatic.git
	cd Flask-Bootstrap-MongoEngine-Fanstatic
	pip install -r requirements.txt
	python runserver.py
	
## Features

* Admin interface at `/admin`
* WTForms example at `/add`

## TODO

* Flask-Login
* Split files structure for models, views and configuration
* Blueprints?