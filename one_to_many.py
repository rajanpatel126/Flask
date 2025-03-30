from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#main application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ipl.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#database object
db = SQLAlchemy(app)

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team = db.Column(db.String(100), nullable=False, unique=True)
    state = db.Column(db.String(100), nullable=False)
    members = db.relationship('Player', backref='team') # not a column, just way to telling alchemy to build relationship
    
    def __repr__(self):
        return f'Team({self.team}, {self.state})'
    
class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    nationality = db.Column(db.String(100), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    
    def __repr__(self):
        return f'Player({self.name}, {self.nationality})'

#server run
if __name__ == '__main__':
    app.run(debug=True)