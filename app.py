from flask import Flask, render_template, url_for

app = Flask(__name__)

# Project data
PROJECTS = {
    "project1": {
        "slug": "project1",
        "title": "Puzzle Game in Scratch",
        "image": "images/project1.svg",
        "description": "A small game where you need to collect crystals and pass 5 levels. Made in Scratch."
    },
    "project2": {
        "slug": "project2",
        "title": "Mini Website in HTML/CSS",
        "image": "images/project2.svg",
        "description": "A landing page about a favorite hobby. Responsive layout, neat cards, and fonts."
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
