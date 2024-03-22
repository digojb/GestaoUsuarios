from Routes.home import home_route
from Routes.cliente import cliente_route
from Database.database import db
from Database.Models.cliente import Cliente

def configure_all(app):
    configure_routes(app)
    configure_db()

def configure_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(cliente_route, url_prefix='/clientes')


def configure_db():
   db.connect()
   db.create_tables([Cliente])