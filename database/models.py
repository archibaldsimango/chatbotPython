from .db import db


class Chat1(db.Document):
    option = db.StringField(required=True, unique=True)
