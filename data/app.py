from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# config sql database 
app.config['SQLAlchemy_DATABASE_URI'] = "sqlite:///saltydatabase.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # supress warning messages

# Instantiate database
db = SQLAlchemy(app)


if __name__ == "__main__":
    app.run(debug=True)