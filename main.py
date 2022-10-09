
from flask import Flask
from flask import jsonify
from config import FLASKS_CONFIGS
from views import apply_views


enviroment = FLASKS_CONFIGS['development']


def create_app(enviroment):
    app = Flask(__name__)
    app.config.from_object(enviroment)
    apply_views(app)
    return app


app = create_app(enviroment)


if __name__ == '__main__':
    app.run(debug=True)
