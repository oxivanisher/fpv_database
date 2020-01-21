from . import db


class YTChannel(db.Model):

    __tablename__ = 'yt_channels'
    id = db.Column(db.Integer, primary_key=True)
    published = db.Column(db.Boolean, unique=False, default=False)
    name = db.Column(db.String(80), unique=True, nullable=False)
    comment = db.Column(db.String(200), unique=False, nullable=False)
    url = db.Column(db.String(80), unique=False, nullable=False)
