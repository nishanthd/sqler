from flask_script import Manager

from sqler import create_app
from sqler import blueprint


app = create_app()
app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)


@manager.command
def run():
    app.run()


if __name__ == '__main__':
    manager.run()