from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)

# configure our database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# we define a class for ORM for the sql alchemy database

db = SQLAlchemy(app)
class Drink(db.Model):
    id = db.Column(db.Integer,primary_key =True)
    name  = db.Column(db.String(80),unique = True, nullable = False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"




@app.route("/")
def index():
    return "HellO"


# we will make a get request
# we make an app to store a drink


@app.route("/drinks")

def get_drinks():

    drinks = Drink.query.all()

    output = [{'name':drink.name, 'description':drink.description} for drink in drinks]

    return {"drinks":output }


@app.route('/drinks/<id>')


def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return {"name":drink.name, "description":drink.description}


@app.route('/drinks', methods = ["POST"])
# we could in theory define everything in one methods

def add_drink():
    # we have to get the request data
    # we are going to gt this by creating  a drink
    drink = Drink(name = request.json['name'], description = request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {'id':drink.id}


@app.route('/drinks/<id>', methods=['DELETE'])

def delete_drink(id):
    drink = Drink.query.get(id)
    if not drink:
        return {"error": "not found"}
    db.session.delete(drink)
    db.session.commit()
    return {"message":"Ahahahaaa"}
