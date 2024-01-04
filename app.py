from flask import Flask, render_template, request, redirect, url_for
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

# Babel configuration
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'

@babel.localeselector
def get_locale():
    return request.args.get('lang') or request.accept_languages.best_match(['en', 'ja'])

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/system')
def system():
    return render_template('system.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
