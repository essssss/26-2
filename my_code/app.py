from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import Employee, Department, db, connect_db, phone_dir_nav

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///employees_db'
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "abc123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)
app.app_context().push()


debug = DebugToolbarExtension(app)
