from flask_mongoengine import MongoEngine

db = MongoEngine()


def initialize_app(app):
    db.init_app(app)
