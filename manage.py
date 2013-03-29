from flask.ext.script import Manager, Server
from application import app
from application.models import User

manager = Manager(app)

# Turn on debugger by default and reloader
manager.add_command("runserver", Server(
    use_debugger=True,
    use_reloader=True,
    host='0.0.0.0',
    port=4000)
)

@manager.command
def create_admin_user():
    """Creates an admin user"""
    email = app.config.get('ADMIN_USER', 'admin@admin.com')
    pwd = app.config.get('ADMIN_PASSWORD', 'secret')
    user = User.by_email(email)
    if user is not None:
        print 'Admin user already there.'
        return
    else:
        user = User(email=email, password=pwd)
        user.save()
        print 'Admin user created.'

if __name__ == "__main__":
    manager.run()