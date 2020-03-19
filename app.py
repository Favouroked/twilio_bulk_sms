from flask import Flask

from controllers.audience import audience
from controllers.templates import templates

app = Flask(__name__)

app.register_blueprint(audience, url_prefix='/audience')
app.register_blueprint(templates, url_prefix='/templates')

if __name__ == '__main__':
    app.run()
