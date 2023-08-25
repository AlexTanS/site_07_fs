from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {"nickname": "Alex"}
    return render_template("index.html",
                           description="Сборник оригинальных фотографий, сделанных в города страны",
                           subject="Фотографии, улица, люди, Москва",
                           title="Фотографии",
                           user=user,
                           )
