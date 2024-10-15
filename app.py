from flask import Flask
from models import *
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///company.db'

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/users')
def users():
    users = User.query.all()
    return[{"id":user.id,"username":user.username,"email":user.email} for user in users]



@app.route('/')
def index():
    return "welcome to flask"

if __name__== '__main__':
    app.run(port=8000, debug=True)