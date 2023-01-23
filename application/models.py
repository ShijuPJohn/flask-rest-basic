from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    posts = db.relationship("Article", cascade="all,delete", backref="author")


class Article(db.Model):
    __tablename__ = "article"
    article_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
