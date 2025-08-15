
from flask import Flask, render_template, url_for

app = Flask(__name__)

# Данные о проектах
PROJECTS = {
    "project1": {
        "slug": "project1",
        "title": "Игра-головоломка на Scratch",
        "image": "images/project1.svg",
        "description": "Небольшая игра, где нужно собрать кристаллы и пройти 5 уровней. Сделано в Scratch."
    },
    "project2": {
        "slug": "project2",
        "title": "Мини-сайт на HTML/CSS",
        "image": "images/project2.svg",
        "description": "Лендинг о любимом хобби. Адаптивная вёрстка, аккуратные карточки и шрифты."
    }
}

@app.route('/')
def index():
    return render_template('index.html', projects=PROJECTS)

@app.route('/project1')
def project1():
    return render_template('project.html', project=PROJECTS["project1"])

@app.route('/project2')
def project2():
    return render_template('project.html', project=PROJECTS["project2"])

if __name__ == '__main__':
    app.run(debug=True)
