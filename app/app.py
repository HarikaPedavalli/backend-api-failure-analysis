from flask import Flask
from routes import report_routes

app = Flask(__name__)
app.register_blueprint(report_routes, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
