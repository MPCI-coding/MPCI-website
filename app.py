from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_babel import Babel
from flask_babel import gettext as _
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, FileField, BooleanField
from wtforms.validators import DataRequired, Email

from dotenv import load_dotenv
import os
import json

def get_locale():
    return request.args.get('lang') or request.accept_languages.best_match(['en', 'ja'])

# Load enviornment variables from .env file
load_dotenv()



app = Flask(__name__)
babel = Babel(app)
babel.init_app(app, locale_selector=get_locale)

# Babel configuration
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'

# Set the secret key from .env file
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Forms:

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    service = SelectField('Service Required', choices=[('consultation', 'Consultation'), ('project', 'Project'), ('other', 'Other')], validators=[DataRequired()])
    layoutAvailable = BooleanField('Is a layout drawing available?')
    layoutDrawing = FileField('Layout Drawing')
    layoutDescription = TextAreaField('Layout Description')
    packingListAvailable = BooleanField('Is a packing list with weights and dimensions of equipment available?')
    packingList = FileField('Packing List')
    packingListDescription = TextAreaField('Packing List Description')
    additionalQuestions = TextAreaField('Any additional questions or clarifications?')


# Routes
@app.route('/')
def index():
    return  render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/system')
def system():
    return render_template('system.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact', methods=['GET'])
def contact():
    form = ContactForm()
    return render_template('contact.html', form=form)

@app.route('/contact-form', methods=['GET', 'POST'])
def contact_form():
    form = ContactForm()
    if request.method == 'POST' and form.validate_on_submit():
        # Process the form data
        print("Form Data:", form.data)
        # Render the confirmation template
        return render_template('contact_form_confirm.html')
    return render_template('contact_form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, port=9000)
