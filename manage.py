from flask_script import Manager

from sql_service import create_app
from sql_service import blueprint


app = create_app()
app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)


@manager.command
def run():
    app.run(host='0.0.0.0', port=5000)


if __name__ == '__main__':
    manager.run()
