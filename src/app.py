from flask import Flask
from controllers import api_controller, app_ui_controller

app = Flask(__name__)

app.register_blueprint(api_controller.bp, url_prefix="/api")
app.register_blueprint(app_ui_controller.bp, url_prefix="/")


if __name__ == "__main__":
    app.run(port=8000, debug=True)
