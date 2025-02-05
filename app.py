from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title="Home")

@app.route('/about')
def about():
    return render_template('about.html', title="About Me")

@app.route('/education')
def education():
    return render_template('education.html', title="Education")

@app.route('/projects')
def projects():
    return render_template('projects.html', title="Projects")

@app.route('/places')
def places():
    return render_template('places.html', title="Visited Places")

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact")

if __name__ == "__main__":
    app.run(debug=True)
