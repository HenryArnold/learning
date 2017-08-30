from flask import Blueprint
main = Blueprint('main', __name__)
from . import views, errors

#regist Blueprint
def create_app(config_name):
    from .main import main as mail_blueprint
    app.register_blueprint(mail_blueparint)

    return app
