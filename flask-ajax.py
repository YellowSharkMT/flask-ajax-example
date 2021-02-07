from flask import Flask, render_template, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect


class Config:
    SECRET_KEY = '111222333444'
    DEBUG = True


app = Flask(__name__)
app.config.from_object(Config)
CSRFProtect(app)


class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])


@app.route('/', endpoint='home', methods=['GET', 'POST'])
def home():
    form = MyForm()
    submitted = False
    message = None
    if form.validate_on_submit():
        submitted = True
        message = 'Success'
    return render_template('home.html', form=form, submitted=submitted, message=message)


@app.route('/angular', endpoint='angular_example', methods=['GET', 'POST'])
def angular_example():
    form = MyForm()
    submitted = False
    message = None
    if form.validate_on_submit():
        submitted = True
        message = 'Success'
    return render_template('home-angular.html', form=form, submitted=submitted, message=message)


@app.route('/my-ajax-endpoint', methods=['POST'])
def ajax_handler():
    form = MyForm()
    if form.validate_on_submit():
        return jsonify({'success': True,
                        'message': 'Success!'})

    return jsonify({'success': False,
                    'message': 'Error - Invalid submission'})


if __name__ == '__main__':
    app.run()
