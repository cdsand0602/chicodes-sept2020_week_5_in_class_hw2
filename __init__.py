from flask import Flask

# Import the Config Object
from config import Config

# Import for the SQLAlchemy Object
from flask_sqlalchemy import SQLAlchemy

# Import the Migrate Object
from flask_migrate import Migrate

app = Flask(__name__)
# Complete the Config cycle for our Flask app
# And Give access to our Database(When we have one)
# Along with our Secret Key
app.config.from_object(Config)

# Init our database (db)
db = SQLAlchemy(app)

# Init the migrator
migrate = Migrate(app,db)

from hw2 import routes,models