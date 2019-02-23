from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import os
import requests
import credentials

# App config.
DEBUG = True
app = Flask(__name__, static_url_path='/static')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'




bike_occupancy_url_template = 'https://api.tfl.gov.uk/Occupancy/BikePoints/{BikePoints_id}'

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])


@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == credentials['password'] and request.form['username'] == credentials['password']:
        session['logged_in'] = True

    else:
        flash('wrong password!')

    return redirect(url_for('bike'))

@app.route("/", methods=['GET', 'POST'])
def bike():
    if not session.get('logged_in'):
        return render_template('login.html')

    else:
        form = ReusableForm(request.form)
        print(form.errors)
        if request.method == 'POST':
            userinput = request.form['name']
            try:
                resp = requests.get('https://api.tfl.gov.uk/Occupancy/BikePoints/{}'.format(userinput))
                bikesPoints = resp.json()
            except Exception as inst:
                print(inst)
                print(resp.reason)
                return

            emptyDock = bikesPoints[0]['emptyDocks']
            location = bikesPoints[0]['name']

        if form.validate():
            # Save the comment here.
            flash('Currently there are' + str(emptyDock) + " available bikes in " + location)
        else:
            flash('Error: no id entered. ')

        return render_template('bike_point_map.html', form=form)

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
app.run(debug=True, host='0.0.0.0', port=5000)