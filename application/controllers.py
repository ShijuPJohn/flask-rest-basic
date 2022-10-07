from flask import render_template, current_app as app

from application.models import Article


@app.route('/', methods=['GET'])
def index_get():
    return render_template("index.html")


@app.route('/articles', methods=['GET'])
def articles_get():
    articles = Article.query.all()
    for arti in articles:
        print(arti.title)
        print(arti.content)
    return render_template("articles.html")
