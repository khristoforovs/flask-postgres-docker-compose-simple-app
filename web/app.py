from flask import Flask
from flask import request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import BaseConfig


app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)


from models import *


@app.route('/', methods=['GET'])
def index():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('index.html', posts=posts)

@app.route('/submit', methods=['POST'])
def submit():
    text = request.form['text']
    post = Post(text)
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
