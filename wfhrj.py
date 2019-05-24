from app import app, db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app.models import product_models, user_models, wxapi_models

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(port=80))


if __name__ == '__main__':
    manager.run()
