from flask import Flask
from views import views

app = Flask(__name__)
app._static_folder = r'C:\Users\hwala\PycharmProjects\AI_Interview_Assistant\static'

app.register_blueprint(views, url_prefix="/")


if __name__ == "__main__":
    app.run(debug=True, port=8000)